from src.pivotal_api_services.pivotal_services import PivotalServices
from src.utils.LoggerHandler import LoggerHandler
from src.utils.file_reader import FileReader
from src.utils.string_handler import StringHandler

logger = LoggerHandler.get_instance()


class WorkspaceServices(PivotalServices):

    def __init__(self):
        super(WorkspaceServices, self).__init__()
        self.__workspaces = "{}/my/workspaces".format(self.request_handler.main_url)
        self.__workspaces_schema_path = "/src/core/api/json_schemas/workspace_schema.json"
        self.workspace = {}
        self.workspaces = {}

    def create_workspace(self, data):
        response = self.request_handler.post_request(endpoint=self.__workspaces, body=data)
        return response.status_code, response.json()

    def update_workspace(self, id, data):
        current_url = self.__workspaces + "/" + id
        response = self.request_handler.put_request(endpoint=current_url, body=data)
        return response.status_code, response.json()

    def get_workspaces(self):
        workspaces_list = self.request_handler.get_request(endpoint=self.__workspaces).json()
        for workspace in workspaces_list:
            if not workspace['name'] in self.workspace:
                self.workspace[workspace['name']] = workspace['id']
        return self.workspace

    def get_workspace(self, id):
        current_url = self.__workspaces + "/" + id
        workspace = self.request_handler.get_request(endpoint=current_url).json()
        if not workspace['name'] in self.workspace:
            self.workspaces[workspace['name']] = workspace['id']
        return workspace

    def delete_workspace(self, id):
        current_url = self.__workspaces + "/" + id
        response = self.request_handler.delete_request(endpoint=current_url)
        return response.status_code

    def get_workspace_schema(self):
        return StringHandler.convert_string_to_json(FileReader.get_file_content(self.__workspaces_schema_path))

