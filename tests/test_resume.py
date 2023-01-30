from pydantic import ValidationError

from parser_tdd.main import Resume
import pytest

data_test_1 = '''
{ 
 "description": "<ul><li>разработка API-запросов,</li><li>работа с бд</li><li>оптимизация SQL-запросов.</li></ul>", 
 "employment": "fullDay", 
 "address": { 
   "region": "Кировская", 
   "city": "Киров", 
   "street_type": "", 
   "street": "", 
   "house_type": "", 
   "house": "", 
   "value": "г Москва, ул Большая Лубянка, 11с1", 
   "lat": 55.763539, 
   "lng": 37.628359 
 }, 
 "name": "Junior Backend-developer", 
 "salary": { 
   "from": 45000, 
   "to": 90000, 
   "currency": "RUR", 
   "gross": false 
 }, 
 "contacts": { 
   "fullName": "Лубянов Алексей", 
   "phone": "79991097659", 
   "email": "lubo.alex@hrb.software" 
 } 
} 
'''

ans_test_1 = {'address': 'г Москва, ул Большая Лубянка, 11с1', 'allow_messages': True,
              'billing_type': 'packageOrSingle', 'business_area': 1,
              'contacts': {'email': 'lubo.alex@hrb.software', 'name': 'Лубянов Алексей',
                           'phone': {'city': '999', 'country': '7', 'number': '109-76-59'}},
              'coordinates': {'latitude': 55.763539, 'longitud': 37.628359},
              'description': '<ul><li>разработка API-запросов,</li><li>работа с бд</li><li>оптимизация SQL-запросов.</li></ul>',
              'experience': {'id': 'noMatter'}, 'html_tags': True,
              'image_url': 'https://img.hhcdn.ru/employer-logo/3410666.jpeg', 'name': 'Junior Backend-developer',
              'salary': 90000, 'salary_range': {'from': 45000, 'to': 90000}, 'schedule': {'id': 'fullDay'}}

data_test_2 = "{}"
data_test_3 = '''
{ 
 "description": "<ul><li>разработка API-запросов,</li><li>работа с бд</li><li>оптимизация SQL-запросов.</li></ul>", 
 "employment": "fullDay", 
 "address": { 
   "region": "Кировская", 
   "city": "Киров", 
   "street_type": "", 
   "street": "", 
   "house_type": "", 
   "house": "", 
   "value": "г Москва, ул Большая Лубянка, 11с1", 
   "lat": 55.763539, 
   "lng": 37.628359 
 }, 
 "name": "Junior Backend-developer", 
 "salary": { 
   "from": 45000, 
   "to": 90000, 
   "currency": "RUR", 
   "gross": false 
 }
} 
'''
data_test_4 = '''
{ 
 "description": "<ul><li>разработка API-запросов,</li><li>работа с бд</li><li>оптимизация SQL-запросов.</li></ul>", 
 "employment": "fullDay", 
 "address": { 
   "region": "Кировская", 
   "city": "Киров", 
   "street_type": "", 
   "street": "", 
   "house_type": "", 
   "house": "", 
   "value": "г Москва, ул Большая Лубянка, 11с1", 
   "lat": 55.763539, 
   "lng": 37.628359 
 }, 
 "name": "Junior Backend-developer", 
 "salary": { 
   "from": 45000, 
   "to": 90000, 
   "currency": "RUR", 
   "gross": false 
 }, 
 "contacts": { 
   "fullName": "Лубянов Алексей", 
   "phone": "79991097659", 
   "email": "lubo.alex@hrb.software" 
 } 
 "hobby": ["football", "chess", "dance"]
} 
'''


@pytest.mark.parametrize("test_input, expected", [(data_test_1, ans_test_1)])
def test_correct_resume(test_input, expected):
    resume = Resume.parse_raw(test_input)
    assert resume.dict() == ans_test_1


@pytest.mark.parametrize("test_input", [data_test_2, data_test_3, data_test_4])
def test_resume_required_data(test_input):
    try:
        resume = Resume.parse_raw(test_input)
        resume.dict()
    except ValidationError as e:
        assert e
