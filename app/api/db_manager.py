from app.api.models import CompaniesIn

from app.api.db import companies, database


async def add_area(payload: CompaniesIn):
    query = companies.insert().values(**payload.dict())
    return await database.execute(query=query)


async def companies():
    query = companies.select()
    return await database.fetch_all(query=query)


async def get_area(id):
    query = companies.select(companies.c.id == id)
    return await database.fetch_one(query=query)


async def delete_area(id: int):
    query = companies.delete().where(companies.c.id == id)
    return await database.execute(query=query)


async def update_area(id: int, payload: CompaniesIn
):
    query = (
        companies
        .update()
        .where(companies.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
