import requests
from behave import given, when, then

BASE_URL = "http://localhost:4567"

@given('I have an existing to-do item with ID "{todo_id}" associated with category ID "{category_id}"')
def step_get_categories(context, todo_id, category_id):
    context.taskID = todo_id
    context.catID = category_id

@given('I have a to-do item ID "{todo_id}" with no association to category ID "{category_id}"')
def step_get_invalid_categories(context, todo_id, category_id):
    context.taskID = todo_id
    context.catID = category_id

@given('I have an invalid to-do item ID "{todo_id}" or category ID "{category_id}"')
def step_get_invalid_any(context, todo_id, category_id):
    context.taskID = todo_id
    context.catID = category_id

@when('I send a DELETE request to "/todos/todo_id/categories/category_id"')
def step_delete_association(context):
    context.response = requests.delete(f"{BASE_URL}/todos/1/categories/1")

@when('I send a DELETE request with wrong category to "/todos/todo_id/categories/category_id"')
def step_delete_inexisting_association(context):
        context.response = requests.delete(f"{BASE_URL}/todos/1/categories/30")

@when('I send a wrong DELETE request to "/todos/todo_id/categories/category_id"')
def step_delete_association(context):
    context.response = requests.delete(f"{BASE_URL}/todos/50/categories/1")

@then('I should receive a "200 OK" status')
def step_response_good_deletion(context):
    requests.post(f"{BASE_URL}/todos/1/categories", json = {"id": "1"}) #reset status after running test
    print(context.response)
    assert context.response.status_code == 200

@then('I should receive a response "404 Not Found" status')
def step_check_failed_result(context):
    assert context.response.status_code == 404

@then('I should receive a response "400 Bad Request" status')
def step_check_failed_all(context):
    assert context.response.status_code == 400