import requests
from behave import given, when, then

BASE_URL = "http://localhost:4567"

@given('I have title "{title}"')
def step_given_title(context, title):
    context.title = title

@given('I have an invalid id 11 but valid title "{title}"')
def step_given_invalid_id(context, title):
    context.title = title

@given('I have a valid completed "{completed}", and valid title "{title}"')
def step_given_title_and_completed(context, title, completed):
    context.title = title
    context.completed = completed.lower() == "true"  

@when('I send a PUT request to "/projects/1" with the valid title "{title}"')
def step_when_put_title(context, title):
    context.response = requests.put(
        f"{BASE_URL}/projects/1", 
        json={"title": title}
    )

@when('I send a PUT request to "/projects/1" with the title "{title}" and completed "{completed}"')
def step_when_put_title_and_completed(context, title, completed):
    context.response = requests.put(
        f"{BASE_URL}/projects/1",
        json={"title": title, "completed": completed.lower() == "true"} 
    )

@when('I send a PUT request to "/projects/11" with a valid title "{title}"')
def step_when_put_invalid_id(context, title):
    context.response = requests.put(
        f"{BASE_URL}/projects/11", 
        json={"title": title}
    )

@then('I should receive a "200 OK" status')
def step_then_check_200_status(context):
    print("Status Code:", context.response.status_code)
    print("Response Body:", context.response.json())
    assert context.response.status_code == 200

@then('I should receive a "404 Not Found" status')
def step_then_check_404_status(context):
    print("Status Code:", context.response.status_code)
    print("Response Body:", context.response.json())
    assert context.response.status_code == 404

