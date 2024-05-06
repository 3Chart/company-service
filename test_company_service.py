import requests


def test_get_all_companies(url: str):
    res = requests.get(url).json()
    assert (res == [{
    'companies_id': 1,
    'name': 'Google',
    'description': 'Мировая технологическая компания, специализирующаяся на поиске в сети Интернет, онлайн-рекламе, облачных вычислениях и других смежных областях.',
    'count_employees': '150,000+',
    'year': '1998'
},
{
    'companies_id': 2,
    'name': 'Apple',
    'description': 'Крупнейший производитель электроники и программного обеспечения, включая iPhone, iPad, MacBook и macOS.',
    'count_employees': '160,000+',
    'year': '1976'
},
{
    'companies_id': 3,
    'name': 'Microsoft',
    'description': 'Мировой лидер в области программного обеспечения, предоставляющий широкий спектр продуктов и услуг, включая операционные системы Windows и облачные сервисы Azure.',
    'count_employees': '180,000+',
    'year': '1975'
},
{
    'companies_id': 4,
    'name': 'Amazon',
    'description': 'Крупнейшая в мире онлайн-торговая платформа и облачный провайдер, предоставляющий широкий спектр услуг, включая электронную коммерцию, облачные вычисления и искусственный интеллект.',
    'count_employees': '1,300,000+',
    'year': '1994'
},
{
    'companies_id': 5,
    'name': 'Facebook',
    'description': 'Социальная сеть, связывающая миллиарды людей по всему миру, а также владелец Instagram, WhatsApp и Oculus.',
    'count_employees': '60,000+',
    'year': '2004'
}])


def test_get_company_by_id(url: str):
    res = requests.get(url).json()
    assert (res == {
    'companies_id': 1,
    'name': 'Google',
    'description': 'Мировая технологическая компания, специализирующаяся на поиске в сети Интернет, онлайн-рекламе, облачных вычислениях и других смежных областях.',
    'count_employees': '150,000+',
    'year': '1998'
})


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/companies/'
    test_get_company_by_id(URL + '1')
    test_get_all_companies(URL)
