"""db di"""
import pinject
from adaptors.mongodb.config import Config
from adaptors.mongodb.mongoadaptor import DataBaseManager
from adaptors.mongodb.utils import AsyncEngine, AsyncMoter
from common_utilities.file_handler import FileUpload
from modules.user.business.utils.password import Password
from modules.user.enterprise.mixins.usermixin import UserMixin
from common_utilities.validators import GetValidator
from adaptors.email_service.email import EmailUtils
from adaptors.sms_service.smsconfig import Config as SmsConfig


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
        bind("fileupload", to_class=FileUpload)
        bind("validator", to_class=GetValidator)
        bind("emailutils", to_class=EmailUtils)
        bind("smsconfig", to_class=SmsConfig)


obj_graph = pinject.new_object_graph(binding_specs=[StartupLaneSpec()])
