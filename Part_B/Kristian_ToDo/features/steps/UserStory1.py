import requests
from behave import given, when, then

BASE_URL = "http://localhost:4567"

@given('I have a valid title "{title}", done status "{doneStatus}", and description "{description}" for the to-do item to be created')
def step_valid_info_check(context, title, doneStatus, description):
    context.title = title
    context.doneStatus = True
    context.description = description

@given('I have the details of a to-do without a title')
def step_invalid_title_check(context):
    context.title = "NULL"

@given('I have a valid title "{title}" for the to-do item to be created')
def step_valid_title_check(context, title):
    context.title = title


@when('I send a POST request to to-dos with the valid title "{title}", description "{description}" and doneStatus "{doneStatus}"')
def step_create_todo_with_data(context, title, description, doneStatus):
    context.response = requests.post(f"{BASE_URL}/todos", 
                            json = {"title": "title", "doneStatus": True, "description": "description"})

@when('I send a POST request to todos with a title "{title}"')
def step_create_todo_with_title(context, title):
    context.response = requests.post(f"{BASE_URL}/todos",
                            json={"title": "title"})

@when ('I send a POST request to todos with the details')
def step_create_todo_no_title(context):
    context.response = requests.post(f"{BASE_URL}/todos", {})

@then('I should receive a 201 created status')
def step_check_response_content(context):
    print(context.response)
    assert context.response.status_code == 201

@then('I should receive a 400 Bad Request status')
def step_check_response_no_title(context):
    assert context.response.status_code == 400
