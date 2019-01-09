from abc import ABCMeta
from src.core.api.request_manager import RequestManager, RequestManagerAccount


class PivotalServices:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.request_handler = RequestManager.get_instance()
        self.request_handler_account = RequestManagerAccount.get_instanceAccount()
        print self.request_handler_account
