Feature: Update a specific project by specifying its id
  As a user, I want to update details of an existing project by its ID so that I can ensure the project information is accurate.

  Scenario Outline: Normal flow - Successfully edit the information of an existing project
    Given I have title "<title>"
    When I send a PUT request to "/projects/1" with the valid title "<title>"
    Then I should receive a "200 OK" status

    Examples:
      | title            |
      | Updated Project  |
      | New Title        |

  Scenario Outline: Alternate flow - Update a project with title and completed field
    Given I have a valid completed "<completed>", and valid title "<title>"
    When I send a PUT request to "/projects/1" with the title "<title>" and completed "<completed>"
    Then I should receive a "200 OK" status

    Examples:
      | title            | completed |
      | Completed Project | true     |
      | Incomplete Project | false  |

  Scenario Outline: Error flow - Attempting to update a project with an invalid id but valid title
    Given I have an invalid id 11 but valid title "<title>"
    When I send a PUT request to "/projects/11" with a valid title "<title>"
    Then I should receive a "404 Not Found" status

    Examples:
      | title           |
      | Invalid Project |


