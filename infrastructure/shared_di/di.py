"""db di"""
import pinject
from mongodb.config import Config
from mongodb.mongoadaptor import DataBaseManager
from mongodb.utils import AsyncEngine, AsyncMoter
from common_utilities.file_handler import FileUpload
from user.business.utils.password import Password
from user.enterprise.mixins.usermixin import UserMixin
from common_utilities.validators import GetValidator
from user_activity_log.enterprise.mixins.user_activity_log_mixin import (
    UserActivityMixin,
)


class StartupLaneSpec(pinject.BindingSpec):
    """_summary_

    Args:
        pinject (_type_): _description_
    """

    def configure(self, bind):
        bind("client", to_class=AsyncMoter)
        bind("engine", to_class=AsyncEngine)
        bind("config", to_class=Config)
        bind("dbmanager", to_class=DataBaseManager)
        bind("utils", to_class=Password)
        bind("usermixin", to_class=UserMixin)
        bind("mixin", to_class=UserActivityMixin)
        bind("fileupload", to_class=FileUpload)
        bind("validator", to_class=GetValidator)


obj_graph = pinject.new_object_graph(binding_specs=[StartupLaneSpec()])
