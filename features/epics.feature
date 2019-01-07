Feature: showing off behave

  @delete_project @delete_epics
  Scenario: Create new epic
    Given I create a project
      | name          |
      | First Project |
    When I create a epic
      | label                  |
      | {"name":"find-rebels"} |
    Then I verify epic created status is 200
    And I verify project schema


  @delete_project @delete_epics
  Scenario: Update the epic
    Given I create a project
      | name          |
      | First Project |
    And I create a epic
      | label                  |
      | {"name":"find-rebels"} |
    When I update a epic
      | label                     |
      | {"name":"updated-rebels"} |
    Then I verify epic updated status is 200
    And I verify project schema

  @delete_project
  Scenario: Delete the epic
    Given I create a project
      | name          |
      | First Project |
    And I create a epic
      | label                  |
      | {"name":"find-rebels"} |
    When I delete the epic
    Then I verify project deleted status is 204