Feature: Delete To-Do Category Association
	As a user, I want to delete an association between a to-do item and a category so that I can reorganize my workspace.

	Scenario: Normal flow - Successfully delete an association
		Given I have an existing to-do item with ID "todo_id" associated with category ID "category_id"
		When I send a DELETE request to "/todos/:todo_id/categories/:category_id"
		Then I should receive a "200 OK" status

	Scenario: Alternate flow - Deleting an already removed association
		Given I have a to-do item ID "todo_id" with no association to category ID "category_id"
		When I send a DELETE request with wrong category to "/todos/todo_id/categories/category_id"
		Then I should receive a response "404 Not Found" status

	Scenario: Error flow - Invalid to-do ID
		Given I have an invalid to-do item ID "todo_id" or category ID "category_id"
		When I send a wrong DELETE request to "/todos/todo_id/categories/category_id"
		Then I should receive a response "404 Not Found" status
