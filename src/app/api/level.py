from typing import List

from app.api import crud
from app.model.level import LevelDB, LevelSchema
from fastapi import APIRouter, HTTPException, Path

router = APIRouter()


@router.post("/levels", response_model=LevelDB, status_code=201)
async def create_level(payload: LevelSchema):
    level_id = await CrudLevel.post(payload)

    response_object = {
        "id": level_id,
        "title": payload.title,
        "description": payload.description,
    }

    return response_object


@router.get("/levels/{id}/", response_model=LevelDB)
async def read_level(id: int = Path(..., gt=0)):
    level = await CrudLevel.get(id)
    if not level:
        raise HTTPException(status_code=404, detail="Level not found")

    return level


@router.get("/levels", response_model=List[LevelDB])
async def read_all_levels():
    return await CrudLevel.get_all()
