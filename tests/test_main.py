def test_get_recipes(client):
    response = client.get("/recipes/")
    assert response.status_code == 200


def test_post_recipe(client):
    response = client.post(
        "/recipes/",
        json={
            "name": "test",
            "cooking_time": 10,
            "ingredients": "test_ingredients",
            "description": "test_description",
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "test",
        "cooking_time": 10,
        "ingredients": "test_ingredients",
        "description": "test_description",
    }


def test_get_recipe_id(client):
    response = client.get("/recipes/1")
    assert response.status_code == 200
    assert response.json() == {
        "name": "test",
        "cooking_time": 10,
        "ingredients": "test_ingredients",
        "description": "test_description",
    }


def test_get_recipe_id_wrong_id(client):
    response = client.get("/recipes/50")
    assert response.status_code == 404
    assert response.json() == {"detail": "Упс! Рецепт не найден!"}


def test_post_recipe_with_wrong_validation(client):
    response = client.post(
        "/recipes/",
        json={
            "name": "test",
            "ingredients": "test_ingredients",
            "description": "test_description",
        },
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "missing",
                "loc": ["body", "cooking_time"],
                "msg": "Field required",
                "input": {
                    "name": "test",
                    "ingredients": "test_ingredients",
                    "description": "test_description",
                },
            }
        ]
    }


def test_post_recipe_with_wrong_type_validation(client):
    response = client.post(
        "/recipes/",
        json={
            "name": "test",
            "cooking_time": "wrong_type",
            "ingredients": "test_ingredients",
            "description": "test_description",
        },
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "int_parsing",
                "loc": ["body", "cooking_time"],
                "msg": "Input should be a valid integer, "
                "unable to parse string as an integer",
                "input": "wrong_type",
            }
        ]
    }


def test_delete_recipe_id(client):
    response = client.delete("/recipes/1")
    assert response.status_code == 200
    assert response.json() == "Товар с id 1 успешно удален!", 200


def test_delete_recipe_id_with_wrong_id(client):
    response = client.delete("/recipes/20")
    assert response.status_code == 404
    assert response.json() == {"detail": "Упс! Рецепт не найден!"}
