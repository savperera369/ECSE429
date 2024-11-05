import requests
from behave import given, when, then

BASE_URL = "http://localhost:4567"

@given('I have an existing to-do item with ID "{id}" that belongs to categories "categories"')
def step_get_categories(context, id):
    context.taskID = id

@given('I have an existing to-do item with ID "{id}" that belongs to no categories')
def step_no_categories(context, id):
    context.taskID = id

@given('I have a existent to-do item ID {id}')
def step_existing(context, id):
    context.taskID = id

@when('I send a GET request to /todos/:id/categories')
def step_get_categories_with_id(context):
    context.response = requests.get(f"{BASE_URL}/todos/1/categories")

@when('I send a GET request to /todos/:id/category')
def step_get_categires_wrong_id(context):
    context.response = requests.get(f"{BASE_URL}/todos/1/category")

@then('I should receive a "404 Not Found" status')
def step_check_failed_response(context):
    print(context.response)
    assert context.response.status_code == 404
