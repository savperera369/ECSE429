import requests
from behave import given, when, then

BASE_URL = "http://localhost:4567"

@given('I have a valid title "{title}"')
def step_valid_title_check(context, title):
    context.title = title
    print(context.title)

@given('I have an invalid field name "{name}"')
def step_invalid_field_check(context, name):
    context.name = name

@given('I add a valid completed "{completed}"')
def step_valid_body_check(context, title, completed):
    context.title = title
    context.completed = completed


@when('I send a POST request to /projects with the valid title "{title}"')
def step_create_project_with_title(context, title):
    context.response = requests.post(f"{BASE_URL}/projects", 
                            json = {"title": title})

@when('I send a POST request to /projects with a title field "{title}" and completed field "{completed}"')
def step_create_project_with_title_and_completed(context, title, completed):
    context.response = requests.post(f"{BASE_URL}/projects",
                            json={"title": title, "completed": True})

@when ('I send a POST request to /projects with an invalid field name "{name}"')
def step_create_project_invalid_field_name(context, name):
    context.response = requests.post(f"{BASE_URL}/projects", json={"name": name})



# @then('I should receive a "{status_code}" status')
# def step_check_status_code_info(context, status_code):
#     assert context.response.status_code == int(status_code)

@then('I should receive a 201 created status')
def step_check_response_content(context):
    print(context.response)
    assert context.response.status_code == 201

@then('I should receive a 400 Bad Request status')
def step_check_response_no_title(context):
    assert context.response.status_code == 400