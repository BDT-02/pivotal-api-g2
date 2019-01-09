Feature: Working workspace

  Scenario: Create new workspace
    Given I create a workspace
      | name            |
      | First Workspace |
    Then I verify workspace creation status is 200
    And I verify workspace schema

  Scenario: Get workspace
    Given I create a workspace
      | name            |
      | First Workspace |
    Then I verify workspace creation status is 200
    And I verify workspace schema

  Scenario: Update the workspace
    Given I create a workspace
      | name          |
      | First workspace |
    When I update the workspace
      | name           |
      | Update workspace |
    Then I verify workspace updated status is 200
    And I verify workspace schema

  Scenario: Delete the workspace
    Given I create a workspace
      | name          |
      | First workspace |
    When I delete the workspace
    Then I verify workspace deleted status is 204