from pydantic import BaseModel, ValidationError, HttpUrl, EmailStr, Field

from typing import Dict, Tuple, Literal, Optional

data = '''
{ 
 "description": "<ul><li>поддержка текущих проектов и сервисов компании,</li><li>разработка новых и доработка существующих функций по техническим заданиям,</li><li>активное взаимодействие с командой разработки,</li><li>освоение новых технологий и развитие профессиональных навыков под руководством опытного наставника.</li><li>Написание автотестов</li></ul>", 
 "employment": "fullDay", 
 "address": { 
   "region": "Кировская", 
   "city": "Киров", 
   "street_type": "", 
   "street": "", 
   "house_type": "", 
   "house": "", 
   "value": "г Киров, ул Володарского, д 157", 
   "lat": 58.593565, 
   "lng": 49.672739 
 }, 
 "name": "Junior Backend-developer", 
 "salary": { 
   "from": 30000, 
   "to": 70000, 
   "currency": "RUR", 
   "gross": false 
 }, 
 "contacts": { 
   "fullName": "Журавлев Илья", 
   "phone": "79536762399", 
   "email": "ilya.zhuravlev@hrb.software" 
 } 
} 
'''


class Address(BaseModel):
    # address: str = Field(alias='value')
    value: str
    lat: float
    lng: float


class Phone(BaseModel):
    city: int
    country: int
    number: str


class Contacts(BaseModel):
    email: EmailStr
    name: str = Field(alias='fullName')
    # phone: Phone


class Coordinates(BaseModel):
    latitude: Address
    longitude: Address


# class Experience(BaseModel):
    # id: str = Field(default='noMatter')


class Salary(BaseModel):
    # from: int
    to: int


# class Schedule(BaseModel):
#     id: str = Field(default='fullDay')
#     id_: str = Field(default='_')


class Resume(BaseModel):
    address: Address
    # allow_messages: bool = Field(default=True)
    # billing_type: str = Field(default='packageOrSingle')
    # business_area: int = Field(default=1)
    # contacts: Contacts
    # # # coordinates: Coordinates
    # description: str
    # experience = dict
    # html_tags = True
    # image_url: HttpUrl = Field(default='https://img.hhcdn.ru/employer-logo/3410666.jpeg')
    # name: str
    # salary: Salary
    # salary_range: Salary = Field(alias='salary', title='salary_range')
    # schedule = dict


try:
    resume = Resume.parse_raw(data)
except ValidationError as e:
    print('Exception', e.json())
else:
    print(resume.json())
