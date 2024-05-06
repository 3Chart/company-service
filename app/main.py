from fastapi import FastAPI, APIRouter
import httpx
from fastapi import APIRouter, HTTPException

app = FastAPI(openapi_url="/api/v1/companies/openapi.json", docs_url="/api/v1/companies/docs")

companies_router = APIRouter()

companies = [
    {
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
    }
]


@companies_router.get("/")
async def read_companies():
    return companies


@companies_router.get("/{companies_id}")
async def read_company(companies_id: int):
    for company in companies:
        if company['companies_id'] == companies_id:
            return company
    return None


app.include_router(companies_router, prefix='/api/v1/companies', tags=['companies'])

if __name__ == '__main__':
    import uvicorn
    import os

    try:
        PORT = int(os.environ['PORT'])
    except KeyError as keyerr:
        PORT = 80
    uvicorn.run(app, host='0.0.0.0', port=PORT)
