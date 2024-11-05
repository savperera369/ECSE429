import requests
from behave import given, when, then

BASE_URL = "http://localhost:4567"

@given('I possess a valid project id "{id}"')
def step_given_valid_project_id(context, id):
    context.project_id = id

@given('I possess an invalid project id "{id}"')
def step_given_invalid_project_id(context, id):
    context.project_id = id

@when('I send a GET request to "/projects/{id}/tasks"')
def step_when_get_project_with_valid_id(context, id):
    context.response = requests.get(f"{BASE_URL}/projects/{id}/tasks")

@when('I make a GET request to "/projects/{id}/tasks" with Accept: application/xml set in my request header')
def step_when_get_project_with_headers(context, id):
    headers = {"Accept": "application/xml"}
    context.response = requests.get(f"{BASE_URL}/projects/{id}/tasks", headers=headers)

@when('I create a GET request to "/projects/{id}/task"')
def step_when_get_project_with_invalid_id(context, id):
    context.response = requests.get(f"{BASE_URL}/projects/{id}/task")

@then('I should be a recipient of a "200 OK" status')
def step_then_check_200_status_get(context):
    assert context.response.status_code == 200, f"Expected 200 but got {context.response.status_code}"

@then('I should be a recipient of a "404 Not Found" status')
def step_then_check_404_status_get(context):
    assert context.response.status_code == 404, f"Expected 404 but got {context.response.status_code}"
