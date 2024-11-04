Feature: To-Do Project Association
	As a user, I want to create a relationship between an existing to-do item and a project so that I can organize my tasks by project.

	Scenario: Normal flow - Successfully create a to-do and project relationship
		Given I have an existing to-do ID "todo_id" and project ID "project_id"
		When I send a POST request to "/todos/todo_id/tasksof" with project ID "project_id" in the body
		Then I should receive a "201 Created" status

	Scenario: Alternate flow - To-do item already assigned to the project
		Given I have an existing to-do ID "todo_id" already related to project ID "project_id"
		When I send a POST request to "/todos/todo_id/tasksof" with existing project ID "project_id" in the body
		Then I should receive a "201 Created" status

	Scenario: Error flow - Non-existent to-do or project ID
		Given I have an invalid to-do ID "todo_id" or project ID "project_id"
		When I send a POST request to "/todos/todo_id/tasksof" with non-existent project ID "project_id" in the body
		Then I should receive a "404 Not Found" status
