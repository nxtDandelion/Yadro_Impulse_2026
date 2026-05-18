from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, BigInteger, String

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True)
    firstname = Column(String, comment="Имя")
    lastname = Column(String, comment="Фамилия")
    fathername = Column(String, comment="Отчество")
    age = Column(BigInteger, comment="Возраст")
    phone = Column(String, comment="Номер телефона")
    email = Column(String, comment="Электронная почта")
    address = Column(String, comment="Адресс")
    gender = Column(String, comment="Пол")

    passport_num = Column(String, comment="Серия и номер паспорта")
    passport_code = Column(String, comment="Код подразделения")
    passport_otd = Column(String, comment="Кем выдан")
    passport_date = Column(String, comment="Дата выдачи")

    inn_fiz = Column(String, comment="ИНН физ.лица")
    inn_ur = Column(String, comment="ИНН юр.лица")
    snils = Column(String, comment="СНИЛС")
    oms = Column(BigInteger, comment="ОМС")
    ogrn = Column(String, comment="ОГРН")
    kpp = Column(BigInteger, comment="КПП")

    bank_bik = Column(BigInteger, comment="БИК банка")
    bank_corr = Column(String, comment="Корреспондентский счет")
    bank_inn = Column(BigInteger, comment="ИНН банка")
    bank_kpp = Column(BigInteger, comment="КПП банка")
    bank_num = Column(String, comment="Номер счета")
    bank_client = Column(String, comment="Имя владельца карты")
    bank_card = Column(String, comment="Номер карты")
    bank_date = Column(String, comment="Срок действия карты")
    bank_cvc = Column(BigInteger, comment="CVC код")

    edu_spec = Column(String, comment="Специальность")
    edu_program = Column(String, comment="Направление")
    edu_name = Column(String, comment="Учебное заведение")
    edu_doc_num = Column(String, comment="Серия и номер диплома")
    edu_reg_num = Column(String, comment="Регистрационный номер")
    edu_year = Column(BigInteger, comment="Дата окончания обучения")

    car_brand = Column(String, comment="Марка автомобиля")
    car_model = Column(String, comment="Модель автомобиля")
    car_year = Column(BigInteger, comment="Год выпуска")
    car_color = Column(String, comment="Цвет")
    car_number = Column(String, comment="Номерной знак")
    car_vin = Column(String, comment="VIN код")
    car_sts = Column(String, comment="Серия и номер СТС")
    car_sts_date = Column(String, comment="Дата выдачи СТС")
    car_pts = Column(String, comment="Серия и номер ПТС")
    car_pts_date = Column(String, comment="Дата выдачи ПТС")
