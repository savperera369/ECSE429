Kristian Myzeqari 261037094

Feature: View Categories
	As a user, I want to view all the categories associated with an existing to-do item so that I can visualize how this task is part of different categories.

	Scenario Outline: Normal flow - Successfully view the categories that are associated with an existing to-do item
		Given I have an existing to-do item with ID "<id>" that belongs to categories "<categories>"
		When I send a GET request to "/todos/<id>/categories"
		Then I should receive a "200 OK" status
		And The response should include the generated id and the title, doneStatus, and the description I provided

	Scenario Outline: Alternate flow - View the categories of a to-do item with no categories
		Given I have an existing to-do item with ID "<id>" that belongs to no categories
		When I send a GET request to "/todos/<id>/categories"
		Then I should receive a "200 OK" status
		And The response should contain an empty list

	Scenario Outline: Error flow - View the categories of a non-existing to-do item
		Given I have a non-existent to-do item ID "<id>"
		When I send a GET request "/todos/<id>/categories"
		Then I should receive a "404 Not Found" status
