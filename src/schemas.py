from pydantic import BaseModel


class BaseRecipe(BaseModel):
    name: str
    cooking_time: int


class Recipes(BaseRecipe):
    ingredients: str
    description: str

    class Config:
        orm_mode = True


class RecipeOut(BaseRecipe):
    views: int
    id: int

    class Config:
        orm_mode = True
