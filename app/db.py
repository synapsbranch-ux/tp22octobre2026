from contextlib import asynccontextmanager

from fastapi import FastAPI
from pymongo import ASCENDING, DESCENDING, AsyncMongoClient

from app import config

mongo_client = AsyncMongoClient(config.MONGO_URL, tz_aware=True)
db = mongo_client[config.MONGO_DB]


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.annonces.create_index([("categorie", ASCENDING), ("created_at", DESCENDING)])
    yield
    await mongo_client.close()
