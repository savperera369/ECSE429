import requests
from behave import given, when, then

BASE_URL = "http://localhost:4567"

@given('I have got a valid project id "{id}"')
def step_given_valid_project_id(context, id):
    context.project_id = id

@given('I have got an invalid project id "{id}"')
def step_given_invalid_project_id(context, id):
    context.project_id = id

@when('I send a GET request to "/projects/{id}"')
def step_when_get_project_with_valid_id(context, id):
    context.response = requests.get(f"{BASE_URL}/projects/{id}")

@when('I make a GET request to "/projects/{id}" with Accept: application/xml set in my request header')
def step_when_get_project_with_headers(context, id):
    headers = {"Accept": "application/xml"}
    context.response = requests.get(f"{BASE_URL}/projects/{id}", headers=headers)

@when('I create a GET request to "/projects/{id}"')
def step_when_get_project_with_invalid_id(context, id):
    context.response = requests.get(f"{BASE_URL}/projects/{id}")

@then('I should be receiving a "200 OK" status')
def step_then_check_200_status_get(context):
    assert context.response.status_code == 200, f"Expected 200 but got {context.response.status_code}"

@then('I should be receiving a "404 Not Found" status')
def step_then_check_404_status_get(context):
    assert context.response.status_code == 404, f"Expected 404 but got {context.response.status_code}"

