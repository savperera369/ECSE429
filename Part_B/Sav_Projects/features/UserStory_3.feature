Feature: Create a specific project without specifying its id
  As a user, I want to create a new project without needing to specify an ID so that I can quickly add projects without managing unique identifiers.

  Scenario: Normal flow - Create a project with only a title field in the request body
    Given I have a valid title "<title>"
    When I send a POST request to /projects with the valid title "<title>"
    Then I should receive a 201 created status

  Scenario: Alternate flow - Successfully create a project with a title field and completed field in the request body
    Given I have a valid title "<title>"
    When I send a POST request to /projects with a title field "<title>" and completed field "<completed>"
    Then I should receive a 201 created status

  Scenario: Error flow - Attempting to create a project with an invalid field in the request body
    Given I have an invalid field name "<name>"
    When I send a POST request to /projects with an invalid field name "<name>"
    Then I should receive a 400 Bad Request status
