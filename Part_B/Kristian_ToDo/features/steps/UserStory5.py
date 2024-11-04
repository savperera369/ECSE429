import requests
from behave import given, when, then

BASE_URL = "http://localhost:4567"

@given('I have an existing to-do ID "{todo_id}" and project ID "{project_id}"')
def step_new_taskof(context, todo_id, project_id):
    context.taskID = todo_id
    context.projID = project_id

@given('I have an existing to-do ID "{todo_id}" already related to project ID "{project_id}"')
def step_existing_taskof(context, todo_id, project_id):    
    context.taskID = todo_id
    context.projID = project_id

@given('I have an invalid to-do ID "{todo_id}" or project ID "{project_id}"')
def step_wrong_id(context, todo_id, project_id):
    context.taskID = todo_id
    context.projID = project_id

@when('I send a POST request to "/todos/todo_id/tasksof" with project ID "project_id" in the body')
def step_new_taskof_association(context):
    context.response = requests.post(f"{BASE_URL}/todos/6/tasksof", 
                                    json = {"id":"2"})

@when('I send a POST request to "/todos/todo_id/tasksof" with existing project ID "project_id" in the body')
def step_existing_taskof_association(context):
    context.response = requests.post(f"{BASE_URL}/todos/6/tasksof",
                                    json = {"id": "2"})

@when('I send a POST request to "/todos/todo_id/tasksof" with non-existent project ID "project_id" in the body')
def step_wrong_id(context):    
    context.response = requests.post(f"{BASE_URL}/todos/1234/tasksof",
                                    json = {"id": "2"})

@then('I should receive a "201 Created" status')
def step_check_new_taskof_response(context):
    context.response.status_code == 201