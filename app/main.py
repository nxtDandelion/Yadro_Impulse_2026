import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.database import get_db, init_db, AsyncSessionLocal
from app.models import User
from app.schemas import UserCreateSchema, TableResponseSchema, UserPageResponseSchema
from contextlib import asynccontextmanager
from math import ceil
import random
import httpx
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    await load(count=100)
    yield

app = FastAPI(lifespan=lifespan)

static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/health")
async def health(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(User))
        return result.scalars().all()
    except Exception as e:
        raise HTTPException(status_code=501, detail=str(e))

@app.get("/api/random", response_model=UserPageResponseSchema)
async def get_random(db: AsyncSession = Depends(get_db)):
    try:
        row_count = await db.execute(select(func.count(User.id)))
        random_id = random.randint(1, row_count.scalar())
        result = await db.execute(select(User).where(User.id == random_id))
        return result.scalar_one_or_none()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/random")
async def get_random_user():
    return FileResponse("static/random_page.html")

@app.get("/api/users", response_model=TableResponseSchema)
async def get_users(page: int = 1, limit: int = 50, db: AsyncSession = Depends(get_db)):
    try:
        offset = (page - 1) * limit
        count = await db.execute(select(func.count(User.id)))
        total = count.scalar()
        pages = ceil(total/limit) if total > 0 else 1
        result = await db.execute(select(User).order_by(User.id).limit(limit).offset(offset))
        users = result.scalars().all()
        return {
            "users": users,
            "total": total,
            "page": page,
            "limit": limit,
            "total_pages": pages,
            "has_next": page < pages,
            "has_prev": page > 1,
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/api/users/{user_id}", response_model=UserPageResponseSchema)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(User).where(User.id == user_id))
        return result.scalars().first()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/{user_id}")
async def get_user_page(user_id: int):
    return FileResponse("static/user_page.html")

@app.get("/", response_class=FileResponse)
async def main_page():
    return FileResponse("static/main_page.html")

@app.post("/")
async def load_users(count:int):
    if count < 1:
        return {"message": "Введите положительное число"}
    await load(count=count)
    return {"status": "ok"}

async def load(count: int):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://api.randomdatatools.ru/?count=" + str(count))
            users_data = response.json()
            async with AsyncSessionLocal() as db:
                if isinstance(users_data, dict):
                    users_data = [users_data]
                for obj in users_data:
                    user_schema = UserCreateSchema(**obj)
                    user_dict = user_schema.model_dump()
                    user = User(**user_dict)
                    db.add(user)
                await db.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')