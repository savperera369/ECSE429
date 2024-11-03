Feature: Getting all projects
	As a user, I want to get all projects so that I can see and manage every project in the system.

	Scenario Outline: Normal flow - Successfully retrieve list of all projects in JSON form.
		Given I have the application running on localhost:4567
		When I send a GET request to "/projects"
		Then I should receive a "200 OK" status
		And the response should include a list of all instances of projects in JSON form
	
	Scenario Outline: Alternate flow - Successfully retrieve list of all projects in XML form
		Given I have the application running 
		When I send a GET request to "/projects" with Accept: application/xml set in my request header
		Then I should receive a "200 OK" status
		And the response should include a list of all instances of projects in XML form

	Scenario Outline: Error flow - Retrieving All Projects without having application running
		Given I don't have the application running on localhost:4567
		When I send a GET request to "/projects" 
		Then I should receive an error message
		And The response should detail ECONNREFUSED 127.0.0.1:4567
