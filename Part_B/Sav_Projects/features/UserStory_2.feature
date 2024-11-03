Feature: Get Details of a specific project by id
	As a user, I want to get details of a specific project by ID so that I can review its information and status.

	Scenario Outline: Normal flow - Successfully retrieve a specific project by id in JSON form
		Given I have a valid id corresponding to one of an existing project
		When I send a GET request to "/projects/:id" with the valid id
		Then I should receive a "200 OK" status
		And the response should include the project with the id that was specified in the endpoint in JSON form
	
	Scenario Outline: Alternate flow - Successfully retrive a specific project by id in XML forn
		Given I have a valid id corresponding to one of an existing project
		When I send a GET request to "/projects/:id" with Accept: application/xml set in my request header
		Then I should receive a "200 OK" status
		And The response should include the project with the id that was specified in the endpoint in XML form

	Scenario Outline: Error flow - Attempting to retrieve a project with an invalid id
		Given I have an invalid id (an id that doesn't correspond to an existing project)
		When I send a GET request to "/projects/:id" with the invalid id
		Then I should receive a "404 Not Found" status
		And the response should indicate that an instance of a project with such id could not be Found
