import requests
from behave import given, when, then

BASE_URL = "http://localhost:4567"

@given('I have new details for the title "{title}", description "{description}", done status "{doneStatus}" of an existing to-do item with ID "{id}"')
def step_new_info_check(context, title, doneStatus, description, id):
    context.title = title
    context.doneStatus = False
    context.description = description
    context.taskID = id

@given('I have new details for the title "{title}" of an existing to-do item with ID "{id}"')
def step_new_title_check(context, title, id):
    context.title = title
    context.taskID = id

@given('I have new details for a to-do item with ID "{id}" that does not exist')
def step_invalid_ID_check(context, id):
    context.title = "newtitle"
    context.taskID = id

@when('I send a PUT request to /todos/:id with the new details')
def step_edit_todo_with_data(context):
    context.response = requests.put(f"{BASE_URL}/todos/1", 
                            json = {"title": "title", "doneStatus": True, "description": "description"})

@when('I send a PUT request to /todos/:id with the new title')
def step_edit_todo_title(context):
    context.response = requests.put(f"{BASE_URL}/todos/1", 
                            json = {"title": "newestTitle"})

@when('I send a PUT request to "/todos/:id" with the details')
def step_edit_invalid_todo(context):
    context.response = requests.put(f"{BASE_URL}/todos/9999", 
                            json = {"title": "newtitle"})

@then('I should receive a 200 OK status')
def step_check_successful_response(context):
    print(context.response.status_code)
    assert context.response.status_code == 200

@then('I should receive a 404 Not Found status')
def step_check_failed_response(context):
    assert context.response.status_code == 404