Feature: Get Details of a specific project by id
	As a user, I want to get details of a specific project by ID so that I can review its information and status.

	Scenario Outline: Normal flow - Successfully retrieve a specific project by id in JSON form
		Given I have got a valid project id "<id>"
		When I send a GET request to "/projects/<id>"
		Then I should receive a "200 OK" status
		
		Examples:
		  | id |
		  | 1  |
	
	Scenario Outline: Alternate flow - Successfully retrive a specific project by id in XML forn
		Given I have got a valid project id "<id>"
		When I make a GET request to "/projects/<id>" with Accept: application/xml set in my request header
		Then I should be receiving a "200 OK" status

		Examples:
		  | id |
		  | 1  |

	Scenario Outline: Error flow - Attempting to retrieve a project with an invalid id
		Given I have got an invalid project id "<id>"
		When I create a GET request to "/projects/<id>"
		Then I should be receiving a "404 Not Found" status
		
		Examples:
		  | id |
		  | 11 |