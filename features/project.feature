Feature: showing off behave

  @delete_project
  Scenario: Create new project
    When I create a project
      | name          |
      | First Project |
    Then I verify project creation status is 200
    And I verify project schema