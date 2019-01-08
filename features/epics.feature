Feature: showing off behave

  @delete_project @delete_epics
  Scenario: Create new epic
    Given I create a project
      | name          |
      | First Project |
    When I create a epic
      | label      |
      | Test epics |
    Then I verify epic created status is 200
    And I verify epic schema


  @delete_project @delete_epics
  Scenario: Update the epic
    Given I create a project
      | name          |
      | First Project |
    And I create a epic
      | label      |
      | Test epics |
    When I update a epic
      | label             |
      | Test Update epics |
    Then I verify epic updated status is 200
    And I verify epic schema

  @delete_project
  Scenario: Delete the epic
    Given I create a project
      | name          |
      | First Project |
    And I create a epic
      | label      |
      | Test epics |
    When I delete the epic
    Then I verify epic updated status is 204