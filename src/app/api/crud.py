from app.model import LevelSchema
from app.config.db import levels, database


async def post(payload: LevelSchema):
    query = levels.insert().values(title=payload.title, description=payload.description)
    return await database.execute(query=query)


async def get(id: int):
    query = levels.select().where(id == levels.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = levels.select()
    return await database.fetch_all(query=query)


async def put(id: int, payload: LevelSchema):
    query = (
        levels
        .update()
        .where(id == levels.c.id)
        .values(title=payload.title, desciption=payload.description)
        .returning(levels.c.id)
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = levels.delete().where(id == levels.c.id)
    return await database.execute(query=query)
