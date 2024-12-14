from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column

from database import Base


class Recipe(Base):
    __tablename__ = "Recipes"

    id = mapped_column(Integer, primary_key=True, index=True)
    name = mapped_column(String, nullable=True)
    cooking_time = mapped_column(String, nullable=True)
    ingredients = mapped_column(String, nullable=True)
    description = mapped_column(String, nullable=True)
    views = mapped_column(Integer, nullable=True, default=0)
