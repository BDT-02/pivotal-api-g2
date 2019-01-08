from src.pivotal_api_services.pivotal_services import PivotalServices
from src.utils.LoggerHandler import LoggerHandler
from src.utils.file_reader import FileReader
from src.utils.string_handler import StringHandler

logger = LoggerHandler.get_instance()

class ProjectServices(PivotalServices):

    def __init__(self):
        super(ProjectServices, self).__init__()
        self.__workspaces = "{}/workspaces".format(self.request_handler.main_url)
        self.__workspaces_schema_path = "/src/core/api/json_schemas/workspaces_schema.json"
        self.__workspaces = {}
        self.__workspaces = {}

    def create_workspace(self, data):
        response = self.request_handler.post_request(endpoint=self.__workspaces, body=data)
        return response.status_code, response.json()

    def get_workspace(self):
        workspaces_list = self.request_handler.get_request(endpoint=self.__workspaces).json()
        for workspace in workspaces_list:
            if not workspace['name'] in self.workspace:
                self.workspace[workspace['name']] = workspace['id']
        return self.workspace

    def get_project(self, id):
        current_url = self.__workspace + "/" + id
        workspace = self.request_handler.get_request(endpoint=current_url).json()
        if not workspace['name'] in self.workspace:
            self.workspaces[workspace['name']] = workspace['id']
        return workspace

    def get_workspaces_schema(self):
        return StringHandler.convert_string_to_json(FileReader.get_file_content(self.__workspace_schema_path))

    def delete_all_workspace(self):
        self.get_workspace()
        for workspace in self.workspace.values():
            url = self.__workspace + "/" + str(workspace)
            logger.info("Deleting %s" % url)
            self.request_handler.delete_request(endpoint=url)