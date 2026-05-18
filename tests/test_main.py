import pytest
from unittest.mock import AsyncMock, Mock, patch, MagicMock
from fastapi import HTTPException
from app.main import load, get_random, get_user
from app.models import User


@pytest.mark.asyncio
async def test_load_single_user():
    mock_user_data = {"FirstName": "John", "LastName": "Doe", "Phone": "123", "Email": "john@test.com"}

    with patch('httpx.AsyncClient') as mock_client:
        mock_response = AsyncMock()
        mock_response.json = Mock(return_value=mock_user_data)
        mock_client.return_value.__aenter__.return_value.get = AsyncMock(return_value=mock_response)

        with patch('app.main.AsyncSessionLocal') as mock_session_local:
            mock_session = MagicMock()
            mock_session.commit = AsyncMock()
            mock_session_local.return_value.__aenter__.return_value = mock_session

            with patch('app.main.UserCreateSchema') as mock_schema:
                mock_schema.return_value.model_dump.return_value = {"firstname": "John", "lastname": "Doe"}

                await load(count=1)

                mock_session.add.assert_called_once()
                mock_session.commit.assert_called_once()


@pytest.mark.asyncio
async def test_load_multiple_users():
    mock_users_data = [
        {"FirstName": "John", "LastName": "Doe", "Phone": "123", "Email": "john@test.com"},
        {"FirstName": "Jane", "LastName": "Smith", "Phone": "456", "Email": "jane@test.com"}
    ]

    with patch('httpx.AsyncClient') as mock_client:
        mock_response = AsyncMock()
        mock_response.json = Mock(return_value=mock_users_data)
        mock_client.return_value.__aenter__.return_value.get = AsyncMock(return_value=mock_response)

        with patch('app.main.AsyncSessionLocal') as mock_session_local:
            mock_session = MagicMock()
            mock_session.commit = AsyncMock()
            mock_session_local.return_value.__aenter__.return_value = mock_session

            with patch('app.main.UserCreateSchema') as mock_schema:
                mock_schema.return_value.model_dump.return_value = {"firstname": "Test"}

                await load(count=2)

                assert mock_session.add.call_count == 2
                mock_session.commit.assert_called_once()


@pytest.mark.asyncio
async def test_load_users_error():
    with patch('httpx.AsyncClient') as mock_client:
        mock_client.return_value.__aenter__.return_value.get = AsyncMock(side_effect=Exception("API Error"))

        with pytest.raises(HTTPException) as exc_info:
            await load(count=5)

        assert exc_info.value.status_code == 500
        assert "API Error" in str(exc_info.value.detail)


@pytest.mark.asyncio
async def test_get_random_user_success():
    mock_session = AsyncMock()

    mock_user = User(id=5, firstname="Random", lastname="User")

    mock_session.execute = AsyncMock()

    mock_count_result = MagicMock()
    mock_count_result.scalar.return_value = 10
    mock_session.execute.return_value = mock_count_result

    mock_user_result = MagicMock()
    mock_user_result.scalar_one_or_none.return_value = mock_user
    mock_session.execute.return_value = mock_user_result

    with patch('app.main.get_db', return_value=mock_session):
        with patch('random.randint', return_value=5):
            result = await get_random(db=mock_session)

            assert result.id == 5
            assert result.firstname == "Random"
            assert result.lastname == "User"


@pytest.mark.asyncio
async def test_get_user_success():
    mock_session = AsyncMock()
    mock_user = User(id=1, firstname="John", lastname="Doe", email="john@test.com")

    mock_result = MagicMock()
    mock_result.scalars.return_value.first.return_value = mock_user

    mock_session.execute = AsyncMock(return_value=mock_result)

    with patch('app.main.get_db', return_value=mock_session):
        result = await get_user(user_id=1, db=mock_session)

        assert result.id == 1
        assert result.firstname == "John"
        assert result.lastname == "Doe"
        assert result.email == "john@test.com"


@pytest.mark.asyncio
async def test_get_user_not_found():
    mock_session = AsyncMock()

    mock_result = MagicMock()
    mock_result.scalars.return_value.first.return_value = None

    mock_session.execute = AsyncMock(return_value=mock_result)

    with patch('app.main.get_db', return_value=mock_session):
        result = await get_user(user_id=999, db=mock_session)

        assert result is None


@pytest.mark.asyncio
async def test_get_user_exception():
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=Exception("Database connection error"))

    with patch('app.main.get_db', return_value=mock_session):
        with pytest.raises(HTTPException) as exc_info:
            await get_user(user_id=1, db=mock_session)

        assert exc_info.value.status_code == 404
        assert "Database connection error" in str(exc_info.value.detail)

