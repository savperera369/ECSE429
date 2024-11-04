import requests
from behave import given, when, then

BASE_URL = "http://localhost:4567"

@given('I have a valid project id "{id}"')
def step_given_valid_project_id(context, id):
    context.project_id = id

@given('I have an invalid project id "{id}"')
def step_given_invalid_project_id(context, id):
    context.project_id = id

@when('I send a DELETE request to "/projects/{id}"')
def step_when_delete_project_with_valid_id(context, id):
    context.response = requests.delete(f"{BASE_URL}/projects/{id}")

@when('I make a DELETE request to "/projects/{id}" with Accept: application/xml set in my request header')
def step_when_delete_project_with_headers(context, id):
    requests.post(f"{BASE_URL}/projects", json={"title": "Sample Project"})
    headers = {"Accept": "application/xml"}
    context.response = requests.delete(f"{BASE_URL}/projects/{id}", headers=headers)

@when('I create a DELETE request to "/projects/{id}"')
def step_when_delete_project_with_invalid_id(context, id):
    context.response = requests.delete(f"{BASE_URL}/projects/{id}")

@then('I should get a "200 OK" status')
def step_then_check_200_status(context):
    assert context.response.status_code == 200, f"Expected 200 but got {context.response.status_code}"

@then('I should get a "404 Not Found" status')
def step_then_check_404_status(context):
    assert context.response.status_code == 404, f"Expected 404 but got {context.response.status_code}"

