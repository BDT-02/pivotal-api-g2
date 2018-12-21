from src.pivotal_api_services.pivotal_services import PivotalServices

class ProjectServices(PivotalServices):

    def __init__(self):
        super(ProjectServices, self).__init__()
        self.__workspaces = "{}/workspaces".format(self.request_handler.main_url)
        self.__workspaces_schema_path = "/src/core/api/json_schemas/workspaces_schema.json"
        self.__workspaces = {}
        self.__workspaces = {}