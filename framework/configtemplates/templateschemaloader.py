from pydantic import BaseModel
from typing import List, Optional
import os
import json


class Initfiles(BaseModel):
    filename: str
    content: List[str]


class Initfolders(BaseModel):
    name: str
    files: List[Initfiles]
    subfolders: Optional[List[object]] = None


class Template(BaseModel):
    name: str
    type: str
    initfolders: Optional[List[Initfolders]] = []
    initfiles: Optional[List[Initfiles]] = []

    def load_from_json(self):
        if not os.getenv("configtemplate"):
            try:
                with open(f"framework/configtemplates/{self.type}.json", "rb") as fs:
                    dataq = json.loads(fs.read())
                    return dataq
            except Exception as e:
                return e.__dict__
        else:
            BASE_DIR = os.getenv("APPROOT")
            os.chdir(BASE_DIR)
            os.chdir(os.getenv("configtemplate"))
            try:
                with open(f"{self.type}.json", "rb") as fs:
                    dataq = json.loads(fs.read())
                    return dataq
            except Exception as e:
                return e.__dict__

    def get_config_instances(self):
        res = []
        for k in self.load_from_json():
            template = Template(
                name=self.name,
                type=self.type,
                initfolders=[Initfolders(name="tests",files=[Initfiles(filename="__init__.py",content=["import {}".format(self.name)])])],
                initfiles=[
                    Initfiles(
                        filename=list(x.keys())[0].format(self.name),
                        content=[
                            x.format(self.name) if "{}" in x else x
                            for x in list(x.values())[0]
                        ],
                    )
                    for x in k["initfiles"]
                ],
            )
            res.append(template)
        return res
    
