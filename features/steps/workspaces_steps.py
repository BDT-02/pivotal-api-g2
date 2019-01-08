import time

from behave import Given, then, step

from src.pivotal_api_services.workspaces import ProjectServices
from src.utils.json_schema_validator import validate_json_schema

workspace_services = ProjectServices()


@Given("I create a workspace")
def create_project_step(context):
    data = {"name": "New workspace1"}
    context.project_status, context.project_response = workspace_services.create_project(data)


@then('I verify workspace creation status is {status_code}')
def step_impl(context, status_code):
    print(context.workspace_status)
    assert context.workspace_status == int(status_code), "Workspace creation status is %s" % status_code


@step('I verify workspace schema')
def step_impl(context):
    actual_response = workspace_services.get_workspace(id=str(context.project_response["id"]))
    schema = workspace_services.get_workspace_schema()
    schema_failure_reason, is_schema_valid = validate_json_schema(schema, actual_response)
    assert is_schema_valid, "Workspace Schema failed due to: {}".format(schema_failure_reason)