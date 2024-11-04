Feature: Delete a specific project by specifying its id
  As a user, I want to delete a specific project by ID so that I can remove completed or irrelevant projects from the system.

  Scenario Outline: Normal flow - Delete a project with a valid id 
    Given I have a valid project id "<id>"
    When I send a DELETE request to "/projects/<id>"
    Then I should get a "200 OK" status

    Examples:
      | id |
      | 1  |

  Scenario Outline: Alternate flow - Delete a project with a valid id and request headers set
    Given I have a valid project id "<id>"
    When I make a DELETE request to "/projects/<id>" with Accept: application/xml set in my request header
    Then I should get a "200 OK" status

    Examples:
      | id |
      | 2  |

  Scenario Outline: Error flow - Attempting to delete a project with an invalid id
    Given I have an invalid project id "<id>"
    When I create a DELETE request to "/projects/<id>"
    Then I should get a "404 Not Found" status

    Examples:
      | id |
      | 11 |
