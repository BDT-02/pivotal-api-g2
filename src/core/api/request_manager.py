from src.core.api.request_handler import RequestHandler
from src.utils.config_handler import ConfigHandler


class RequestManager:
    __instance = None

    @staticmethod
    def get_instance():
        if RequestManager.__instance is None:
            RequestManager.__instance = RequestHandler()
            RequestManager.__instance.session.headers.update(
                {"X-TrackerToken": ConfigHandler.get_config().get_token(),
                 "Content-Type": "application/json"})
        return RequestManager.__instance


class RequestManagerAccount:
    __instance_account = None

    @staticmethod
    def get_instanceAccount():
        if RequestManagerAccount.__instance_account is None:
            RequestManagerAccount.__instance_account = RequestHandler()
            RequestManagerAccount.__instance_account.session.headers.update(
                {"X-CSRF-Token": ConfigHandler.get_config().get_xcsrftoken(),
                 "Content-Type": "application/json",
                 "X-Requested-With": "XMLHttpRequest",
                 "Cookie": ConfigHandler.get_config().get_cookie()})
        return RequestManagerAccount.__instance_account
