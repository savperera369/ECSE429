Feature: Create a new To-do item
	As a user, I want to create a new to-do item so that I can keep track of my tasks

	Background:
		Given the REST API is running

	Scenario Outline: Normal flow - Successfully create a new to-do item.
		Given I have a valid title, doneStatus, and description for the to-do item to be created
		When I send a POST request to "/todos" with the valid details
		Then I should receive a "201 Created" status
		And The response should include the generated id and the title, doneStatus, and the description I provided
	
	Scenario Outline: Alternate flow - Successfully create a new to-do item with only a valid title
		Given I have a valid title for the to-do item to be created
		When I send a POST request to "/todos" with a title
		Then I should receive a "201 Created" status
		And The response should include the the generated id, title I provided, and default values false and empty for the doneStatus and description respectively

	Scenario Outline: Error flow - Creating a to-do without a title
		Given I have the details of a to-do without a title
		When I send a POST request to "/todos" with the details
		Then I should receive a "400 Bad Request" status
		And The response should indicate which mandatory field is missing
