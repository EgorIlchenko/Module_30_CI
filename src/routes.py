from typing import List
from fastapi import APIRouter, HTTPException
from database import engine, session, Base
import schemas
from models import Recipe
from sqlalchemy.future import select


router = APIRouter()


@router.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@router.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()


@router.get('/recipes/', response_model=List[schemas.RecipeOut])
async def recipes() -> List[schemas.RecipeOut]:
    result = await session.execute(select(Recipe).
                                   order_by(Recipe.views.desc(),
                                            Recipe.cooking_time))

    return result.scalars().all()


@router.get('/recipes/{id}', response_model=schemas.Recipes)
async def recipe_id(id: int) -> schemas.Recipes:
    result = await session.execute(
        select(Recipe).filter_by(id=id)
    )
    record = result.scalars().first()

    if record is None:
        raise HTTPException(status_code=404, detail="Упс! Рецепт не найден!")

    record.views += 1
    await session.commit()

    return record


@router.post('/recipes/', response_model=schemas.Recipes)
async def recipe(recipe: schemas.Recipes) -> Recipe:
    new_recipe = Recipe(**recipe.dict())
    async with session.begin():
        session.add(new_recipe)
    return new_recipe


@router.delete('/recipes/{id}')
async def delite_recipe(id: int) -> str:
    result = await session.execute(select(Recipe).filter_by(id=id))
    record = result.scalars().first()

    if record is None:
        raise HTTPException(status_code=404, detail="Упс! Рецепт не найден!")

    await session.delete(record)
    await session.commit()

    return f"Товар с id {id} успешно удален!"