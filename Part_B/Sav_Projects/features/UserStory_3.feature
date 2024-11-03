Feature: Create a specific project without specifying its id
    As a user, I want to create a new project without needing to specify an ID so that I can quickly add projects without managing unique identifiers.

	Scenario Outline: Normal flow - Create a project with only a title field in the request body
		Given I have a request body that includes a title field
		When I send a POST request to "/projects" with the above specified request body
		Then I should receive a "201 Created" status
		And the response should include a project instance with the above specified title field.
	
	Scenario Outline: Alternate flow - Successfully create a project with a title field and completed field in the request body
		Given I have a request body with a title field and completed field
		When I send a POST request to "/projects" with the above specified request body
		Then I should receive a "201 Created" status
		And The response should include a project instance with the above specified title field and completed field.

	Scenario Outline: Error flow - Attempting to create a project with an invalid field in the request body
		Given I have a request body with an invalid field like name
		When I send a POST request to "/projects" with the invalid request body
		Then I should receive a "400 Bad Request" status
		And the response should indicate that the invalid field could not be found