from pydantic import BaseModel, Field
from typing import Optional, List


class UserCreateSchema(BaseModel):
    firstname : Optional[str] = Field(None, alias="FirstName")
    lastname : Optional[str] = Field(None, alias="LastName")
    fathername : Optional[str] = Field(None, alias="FatherName")
    age : Optional[int] = Field(None, alias="YearsOld")
    phone: Optional[str] = Field(None, alias="Phone")
    email: Optional[str] = Field(None, alias="Email")
    address: Optional[str] = Field(None, alias="Address")
    gender: Optional[str] = Field(None, alias="Gender")

    passport_num: Optional[str] = Field(None, alias="PasportNum")
    passport_code: Optional[str] = Field(None, alias="PasportCode")
    passport_otd: Optional[str] = Field(None, alias="PasportOtd")
    passport_date : Optional[str] = Field(None, alias="PasportDate")

    inn_fiz : Optional[str] = Field(None, alias="inn_fiz")
    inn_ur : Optional[str] = Field(None, alias="inn_ur")
    snils : Optional[str] = Field(None, alias="snils")
    oms : Optional[int] = Field(None, alias="oms")
    ogrn : Optional[str] = Field(None, alias="ogrn")
    kpp : Optional[int] = Field(None, alias="kpp")

    bank_bik : Optional[int] = Field(None, alias="bankBIK")
    bank_corr : Optional[str] = Field(None, alias="bankCorr")
    bank_inn : Optional[int] = Field(None, alias="bankINN")
    bank_kpp : Optional[int] = Field(None, alias="bankKPP")
    bank_num : Optional[str] = Field(None, alias="bankNum")
    bank_client: Optional[str] = Field(None, alias="bankClient")
    bank_card : Optional[str] = Field(None, alias="bankCard")
    bank_date : Optional[str] = Field(None, alias="bankDate")
    bank_cvc : Optional[int] = Field(None, alias="bankCVC")

    edu_spec : Optional[str] = Field(None, alias="EduSpecialty")
    edu_program : Optional[str] = Field(None, alias="EduProgram")
    edu_name : Optional[str] = Field(None, alias="EduName")
    edu_doc_num : Optional[str] = Field(None, alias="EduDocNum")
    edu_reg_num : Optional[str] = Field(None, alias="EduRegNumber")
    edu_year : Optional[int] = Field(None, alias="EduYear")

    car_brand : Optional[str] = Field(None, alias="CarBrand")
    car_model : Optional[str] = Field(None, alias="CarModel")
    car_year : Optional[int] = Field(None, alias="CarYear")
    car_color : Optional[str] = Field(None, alias="CarColor")
    car_number : Optional[str] = Field(None, alias="CarNumber")
    car_vin : Optional[str] = Field(None, alias="CarVIN")
    car_sts : Optional[str] = Field(None, alias="CarSTS")
    car_sts_date : Optional[str] = Field(None, alias="CarSTSDate")
    car_pts : Optional[str] = Field(None, alias="CarPTS")
    car_pts_date : Optional[str] = Field(None, alias="CarPTSDate")

class UserResponseSchema(BaseModel):
    id: int
    firstname : str
    lastname : str
    phone : str
    email : str
    address : str
    gender : str

class TableResponseSchema(BaseModel):
    users : List[UserResponseSchema]
    total : int
    page : int
    limit : int
    total_pages : int
    has_next : bool
    has_prev : bool

class UserPageResponseSchema(BaseModel):
    id : int
    firstname : str
    lastname : str
    fathername : str
    age : int
    phone : str
    email : str
    address : str
    gender : str

    passport_num : str
    passport_code : str
    passport_otd : str
    passport_date : str

    inn_fiz : str
    inn_ur : str
    snils : str
    oms : int
    ogrn : str
    kpp : int

    bank_bik : int
    bank_corr : str
    bank_inn : int
    bank_kpp : int
    bank_num : str
    bank_client : str
    bank_card : str
    bank_date : str
    bank_cvc : int

    edu_spec : str
    edu_program : str
    edu_name : str
    edu_doc_num : str
    edu_reg_num : str
    edu_year : int

    car_brand : str
    car_model : str
    car_year : int
    car_color : str
    car_number : str
    car_vin : str
    car_sts : str
    car_sts_date : str
    car_pts : str
    car_pts_date : str