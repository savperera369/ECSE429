Feature: Getting all todos related to a project
	As a user, I want to get all todos of a specific project so that I can see and manage the todos of that project in the system.

	Scenario Outline: Normal flow - Successfully retrieve todos of a specific project by id in JSON form
		Given I possess a valid project id "<id>"
		When I send a GET request to "/projects/<id>/tasks"
		Then I should receive a "200 OK" status
		
		Examples:
		  | id |
		  | 1  |
	
	Scenario Outline: Alternate flow - Successfully retrive todos of a specific project by id in XML forn
		Given I possess a valid project id "<id>"
		When I make a GET request to "/projects/<id>/tasks" with Accept: application/xml set in my request header
		Then I should be a recipient of a "200 OK" status

		Examples:
		  | id |
		  | 1  |

	Scenario Outline: Error flow - Attempting to retrieve todos of a project with an invalid id
		Given I possess an invalid project id "<id>"
		When I create a GET request to "/projects/<id>/task"
		Then I should be a recipient of a "404 Not Found" status
		
		Examples:
		  | id |
		  | 1 |
