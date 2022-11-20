import importlib
import json
from xml.dom import ValidationErr


class GetValidator:
    def get_validator(self, dtoname: object):
        dtoname = dtoname.__class__.__name__
        fs = open("./common_utilities/validators/validator_config.json", "rb")
        print(fs, "testss")
        file_ = json.load(fs)
        for i in file_:
            if i["dtoname"] == dtoname:
                validator = importlib.import_module(i["validator_class"][0])
                return getattr(validator, i["validator_class"][1])

        return None
