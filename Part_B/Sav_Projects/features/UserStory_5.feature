Feature: Delete a specific project by specifying its id
    As a user, I want to delete a specific project by ID so that I can remove completed or irrelevant projects from the system.

	Scenario Outline: Normal flow - Delete a project with a valid id 
		Given I have a valid project id
		When I send a DELETE request to "/projects/:id" with the valid project id
		Then I should receive a "200 OK" status
		And the response body should be empty
	
	Scenario Outline: Alternate flow - Delete a project with a valid id with request headers set
		Given I have a valid project id
		When I send a DELETE request to "/projects/:id" with Accept: application/xml set in my request header
		Then I should receive a "200 OK" status
		And the response body should be empty

	Scenario Outline: Error flow - Attempting to delete a project with an invalid id
		Given I have an invalid project id
		When I send a DELETE request to "/projects/:id" with the invalid id
		Then I should receive a "404 Not Found" status
		And the response should indicate that a project with the specified id could not be found