from parser_tdd.main import Resume, data


def test_resume_not_empty():
    assert data != "{}"


def test_correct_type_data():
    resume = Resume.parse_raw(data)
    assert resume.dict()


def test_correct_resume():
    resume = Resume.parse_raw(data)
    list_keys = ['address', 'allow_messages', 'billing_type', 'business_area',
                 'contacts', 'coordinates', 'description', 'experience', 'html_tags',
                 'image_url', 'name', 'salary', 'salary_range', 'schedule']
    acc = 0
    for keys in resume.dict():
        if keys not in list_keys:
            acc += 1
            break
    assert acc == 0
