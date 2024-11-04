Feature: Update a To-do item
	As a user, I want to update an existing to-do item so that I can replace the task's information in one request if needed.

	Scenario: Normal flow - Successfully edit the information of an existing to-do item
		Given I have new details for the title "title", description "description", done status "doneStatus" of an existing to-do item with ID "1"
		When I send a PUT request to /todos/:id with the new details
		Then I should receive a 200 OK status

	Scenario: Alternate flow - Editing some information of an existing to-do item
		Given I have new details for the title "title" of an existing to-do item with ID "1"
		When I send a PUT request to /todos/:id with the new title
		Then I should receive a 200 OK status

	Scenario: Error flow - Attempting to edit the information of a to-do item that does not exist
		Given I have new details for a to-do item with ID "9999" that does not exist
		When I send a PUT request to "/todos/:id" with the details
		Then I should receive a 404 Not Found status
