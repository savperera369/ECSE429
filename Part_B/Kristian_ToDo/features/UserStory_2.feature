Kristian Myzeqari 261037094

Feature: Update an existing To-do item
	As a user, I want to update an existing to-do item so that I can replace the task's information in one request if needed.
	
	Background:
		Given I have an existing to-do item with ID "<id>"

	Scenario Outline: Normal flow - Successfully edit the information of an existing to-do item
		Given I have new details for the title, description, doneStatus of an existing to-do item with ID "<id>"
		When I send a PUT request to "/todos/<id>" with the new details
		Then I should receive a "200 Ok" status
		And The response should include the generated id and the title, doneStatus, and the description I provided

	Scenario Outline: Alternate flow - Editing some information of an existing to-do item
		Given I have new details for the title of an existing to-do item with ID "<id>"
		When I send a PUT request to "/todos/<id>" with the new details
		Then I should receive a "200 Ok" status
		And The response should include the body of the updated to-do item with the given name, and default values for the doneStatus and description fields

	Scenario Outline: Error flow - Attempting to edit the information of a to-do item that does not exist
		Given I have new details for a to-do item with ID "<id>" that does not exist
		When I send a PUT request to "/todos/<id>" with the details
		Then I should receive a "404 Not Found" status
		And The response should specify the reason the response failed
