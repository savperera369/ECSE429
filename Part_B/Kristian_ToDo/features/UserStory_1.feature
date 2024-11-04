Feature: Create To-do Item
	As a user, I want to create a new to-do item so that I can keep track of my tasks

	Scenario: Normal flow - Successfully create a new to-do item
		Given I have a valid title "title", done status "true", and description "description" for the to-do item to be created
		When I send a POST request to to-dos with the valid title "title", description "description" and doneStatus "true"
		Then I should receive a 201 created status
	
	Scenario: Alternate flow - Successfully create a new to-do item with only a valid title
		Given I have a valid title "title" for the to-do item to be created
		When I send a POST request to todos with a title "title"
		Then I should receive a 201 created status

	Scenario: Error flow - Creating a to-do without a title
		Given I have the details of a to-do without a title
		When I send a POST request to todos with the details
		Then I should receive a 400 Bad Request status
