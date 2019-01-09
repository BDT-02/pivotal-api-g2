import time

from behave import Given, then, step

from src.pivotal_api_services.workspaces import WorkspaceServices
from src.utils.json_schema_validator import validate_json_schema

workspace_services = WorkspaceServices()


@Given("I create a workspace")
def create_project_step(context):
    data = {"name": "New workspace1"}
    context.workspace_status, context.workspace_response = workspace_services.create_workspace(data)


@step("I update the workspace")
def update_workspace_step(context):
    data = {}
    for row in context.table:
        data = {"name": str(row['name'])}
    context.workspace_status, context.project_response = workspace_services.update_workspace(
        id=str(context.workspace_response["id"]), data=data)


@step("I delete the workspace")
def update_workspace_step(context):
    context.workspace_status = workspace_services.delete_workspace(id=str(context.project_response["id"]))


@then('I verify workspace updated status is {status_code}')
def step_impl(context, status_code):
    print(context.workspace_status)
    assert context.workspace_status == int(status_code), "Workspace updated status is %s" % status_code


@then('I verify workspace {method_verb} status is {status_code}')
def step_impl(context, method_verb, status_code):
    print(context.workspace_status)
    assert method_verb.lower() in ["creation", "delete"]
    assert context.workspace_status == int(status_code), "Workspace %s status is %s" % (method_verb, status_code)


@step('I verify workspace schema')
def step_impl(context):
    actual_response = workspace_services.get_workspace(id=str(context.project_response["id"]))
    schema = workspace_services.get_workspace_schema()
    schema_failure_reason, is_schema_valid = validate_json_schema(schema, actual_response)
    assert is_schema_valid, "Workspace Schema failed due to: {}".format(schema_failure_reason)
