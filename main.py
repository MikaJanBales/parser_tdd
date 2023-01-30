from pydantic import BaseModel, ValidationError, HttpUrl, EmailStr, Field, validator

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


class Contacts(BaseModel):
    email: EmailStr
    name: str = Field(alias="fullName")
    phone: str

    @validator("phone")
    def phone_number(cls, v):
        d = {
            "city": v[1:4],
            "country": v[0],
            "number": v[4:7] + '-' + v[7:9] + '-' + v[9:]
        }
        return d


class Resume(BaseModel):
    address: dict
    allow_messages: bool = Field(default=True)
    billing_type: str = Field(default="packageOrSingle")
    business_area: int = Field(default=1)
    contacts: Contacts
    coordinates: dict = Field(alias="address")
    description: str
    experience: dict = Field(default={"id": "noMatter"})
    html_tags: bool = Field(default=True)
    image_url: HttpUrl = Field(default='https://img.hhcdn.ru/employer-logo/3410666.jpeg')
    name: str
    salary: dict
    salary_range: dict = Field(alias="salary")
    schedule: str = Field(alias="employment")

    @validator("address")
    def address_value(cls, v):
        v = v["value"]
        return v

    @validator("coordinates")
    def coordinate(cls, v):
        d = {
            "latitude": v["lat"],
            "longitud": v["lng"]
        }
        return d

    @validator("salary")
    def good_salary(cls, v):
        ans = v["to"]
        return ans

    @validator("salary_range")
    def from_salary_to(cls, v):
        v.pop("currency")
        v.pop("gross")
        return v

    @validator("schedule")
    def schedule_employ(cls, v):
        d = {"id": v}
        return d


try:
    resume = Resume.parse_raw(data)
except ValidationError as e:
    print("Exception", e.json())
else:
    print(resume.dict())
