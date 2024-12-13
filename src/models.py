from sqlalchemy import Column, String, Integer
from database import Base


class Recipe(Base):
    __tablename__ = "Recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    cooking_time = Column(String, nullable=True)
    ingredients = Column(String, nullable=True)
    description = Column(String, nullable=True)
    views = Column(Integer, nullable=True, default=0)
