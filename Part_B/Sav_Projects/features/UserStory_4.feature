Feature: Update a specific project by specifying its id
    As a user, I want to update details of an existing project by its ID so that I can ensure the project information is accurate.

	Scenario Outline: Normal flow - Update a project with a valid id specifying only a title field in the request body
		Given I have a valid id and request body that includes a title field
		When I send a PUT request to "/projects/:id" with the above specified request body
		Then I should receive a "200 OK" status
		And the response should include the modified project instance with the above specified title field.
	
	Scenario Outline: Alternate flow - Update a project with a valid id specifying the title field and completed field in the request body
		Given I have a valid id and request body with a title field and completed field
		When I send a PUT request to "/projects/:id" with the above specified request body
		Then I should receive a "200 OK" status
		And the response should include the modified project instance with the above specified title field and completed field.

	Scenario Outline: Error flow - Attempting to update a project with an invalid id
		Given I have an invalid project id and a valid request body
		When I send a PUT request to "/projects/:id" with the valid request body
		Then I should receive a "404 Not Found" status
		And the response should indicate that the project id is invalid