from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_recipes():
    response = client.get('/recipes/')
    assert response.status_code == 200


def test_get_recipe_id():
    response = client.get('/recipes/5')
    assert response.status_code == 200
    assert response.json() == {
      "name": "test",
      "cooking_time": 10,
      "ingredients": "test_ingredients",
      "description": "test_description"
    }


def test_get_recipe_id_wrong_id():
    response = client.get('/recipes/50')
    assert response.status_code == 404
    assert response.json() == {"detail": "Упс! Рецепт не найден!"}


def test_post_recipe():
    response = client.post('/recipes/',
                           json={"name": "test",
                                 "cooking_time": 10,
                                 "ingredients": "test_ingredients",
                                 "description": "test_description"})
    assert response.status_code == 200
    assert response.json() == {
        "name": "test",
        "cooking_time": 10,
        "ingredients": "test_ingredients",
        "description": "test_description"
    }


def test_post_recipe_with_wrong_validation():
    response = client.post('/recipes/',
                           json={"name": "test",
                                 "ingredients": "test_ingredients",
                                 "description": "test_description"})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "missing",
                "loc": [
                    "body",
                    "cooking_time"
                ],
                "msg": "Field required",
                "input": {
                    "name": "test",
                    "ingredients": "test_ingredients",
                    "description": "test_description"
                  }
                }
              ]
            }


def test_post_recipe_with_wrong_type_validation():
    response = client.post('/recipes/',
                           json={"name": "test",
                                 "cooking_time": "wrong_type",
                                 "ingredients": "test_ingredients",
                                 "description": "test_description"})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "int_parsing",
                "loc": [
                    "body",
                    "cooking_time"
                    ],
                "msg": "Input should be a valid integer, unable to parse string as an integer",
                "input": "wrong_type"
            }
        ]
    }


def test_delete_recipe_id():
    response = client.delete('/recipes/6')
    assert response.status_code == 200
    assert response.json() == "Товар с id 6 успешно удален!", 200


def test_delete_recipe_id_with_wrong_id():
    response = client.delete('/recipes/20')
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Упс! Рецепт не найден!"
    }
