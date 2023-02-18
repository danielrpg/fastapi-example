from fastapi import FastAPI
from app.config.db import engine, metadata, database
from app.api import level

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.connect()


app.include_router(level.router)
