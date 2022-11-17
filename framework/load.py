from typing import Dict
import os
import json
import pip
import asyncio
import importlib
from pydantic import BaseModel


class ResponseCommand(BaseModel):
    response: str
    process_status: bool


class LoadComponents:
    """_summary_

    Returns:
        _type_: _description_
    """

    FRAMEWORK_REGISTRY = ""

    def __init__(self) -> None:
        if os.getenv("FRAMEWORK_REGISTRY") is not None:
            self.FRAMEWORK_REGISTRY = os.getenv("FRAMEWORK_REGISTRY")
        else:
            self.FRAMEWORK_REGISTRY = asyncio.run(self.format_config())[
                "FRAMEWORK_REGISTRY"
            ]

    async def install(self, package, app=None, adaptors=None):
        if hasattr(pip, "main"):
            pip.main(["install", package])
            dirs = package.split("=")
            dirsd = None
            if "/" in dirs[-1]:
                dirsd = dirs[-1].split("/")[-1]
            else:
                dirsd = dirs[-1]
            os.makedirs(dirsd)
            os.chdir(dirsd)
            with open("__init__.py", "w+") as fs:
                if app is None and adaptors is None:
                    fs.writelines(f"from {dirsd} import business,enterprise")
                elif app is not None:
                    fs.writelines(f"from {dirsd} import routes")
                elif adaptors is not None:
                    fs.writelines(f"import {dirsd}")
                fs.close()
                return ResponseCommand(
                    response="package installed and module initiated",
                    process_status=True,
                )
        else:
            pip._internal.main(["install", package])
            return ResponseCommand(
                response="something went wrong", process_status=False
            )

    async def format_config(self, **kwargs):
        with open("framework/framework_config.json", "rb") as fs:
            data = json.load(fs)
            fs.close()
            return ResponseCommand(response=data, process_status=True)

    async def load(self, **kwargs) -> Dict[str, str]:
        """_summary_
        {'name':string,'type':string,'from':string,'path':Optional[string]}
        Returns:
            Dict[str,str]: _description_
        """
        if (
            "type" in list(kwargs.keys())
            and kwargs["type"] == "modules"
            or kwargs["type"] == "adaptors"
        ):
            return await self.modules(**kwargs)
        return ResponseCommand(
            response="type and from kwargs are required", process_status=False
        )

    async def modules(self, **kwargs):
        if "type" in list(kwargs.keys()) and kwargs["type"] == "modules":
            if "path" not in list(kwargs.keys()):
                data = {
                    "from": kwargs.get("from"),
                    "name": kwargs.get("name"),
                    "type": kwargs.get("type"),
                }
            else:
                data = {
                    "from": kwargs.get("from"),
                    "name": kwargs.get("name"),
                    "type": kwargs.get("type"),
                    "path": kwargs.get("path"),
                }

            resp = await self.from_(**data)
            return ResponseCommand(response=resp, process_status=True)
        elif "type" in list(kwargs.keys()) and kwargs["type"] == "adaptors":
            if "path" not in list(kwargs.keys()):
                data = {
                    "from": kwargs.get("from"),
                    "name": kwargs.get("name"),
                    "type": kwargs.get("type"),
                }
            else:
                data = {
                    "from": kwargs.get("from"),
                    "name": kwargs.get("name"),
                    "type": kwargs.get("type"),
                    "path": kwargs.get("path"),
                }
            resp = await self.from_(**data)
            return ResponseCommand(response=resp, process_status=True)

    async def load_application(self, **kwargs):
        if "from" in list(kwargs.keys()) and kwargs["from"] == "FRAMEWORK_REGISTRY":
            with open("config.json", "w+") as fs:
                data = json.loads(fs.read())
            os.chdir(data["app_path"])
            name = kwargs.get("name")
            url = (
                self.FRAMEWORK_REGISTRY
                + f"infrastructure/server/app/application/{name}"
            )
            self.install(url, app=True)
            dependency_modules = importlib.__import__("dependency_modules")
            dependency_adaptors = importlib.__import__("dependency_adaptors")
            dependency_common_utilities = importlib.__import__(
                "dependency_common_utilities"
            )
            if dependency_modules != []:
                for ij in dependency_modules:
                    await self.load(**ij)
            if dependency_adaptors != []:
                for ij in dependency_adaptors:
                    await self.load(**ij)
            if dependency_common_utilities != []:
                for ij in dependency_common_utilities:
                    await self.load(**ij)
            return ResponseCommand(response="app loaded", process_status=True)

    async def from_(self, **kwargs):
        type = kwargs.get("type")
        if "from" in list(kwargs.keys()) and kwargs["from"] == "FRAMEWORK_REGISTRY":
            if "path" not in list(kwargs.keys()):
                os.chdir(kwargs.get("type"))
            else:
                os.chdir(kwargs.get("path"))
            try:
                if kwargs.get("type") == "adaptors":
                    await self.install(
                        self.FRAMEWORK_REGISTRY
                        + kwargs.get("type")
                        + "/"
                        + kwargs.get("name"),
                        adaptors=True,
                    )
                else:
                    await self.install(
                        self.FRAMEWORK_REGISTRY
                        + kwargs.get("type")
                        + "/"
                        + kwargs.get("name")
                    )
            except Exception as e:
                return ResponseCommand(response=e, process_status=False)
            if "path" not in list(kwargs.keys()):
                os.chdir("../")
            else:
                path = kwargs.get("path").split("/")
                for fr in path:
                    os.chdir("../")
            return ResponseCommand(
                response=f"{type} loaded sucessfully", process_status=True
            )
        elif "from" in list(kwargs.keys()) and kwargs["from"] == "GIT_URL":
            if "path" not in list(kwargs.keys()):
                os.chdir(kwargs.get("type"))
            else:
                os.chdir(kwargs.get("path"))
            try:
                if kwargs.get("type") == "adaptors":
                    await self.install(
                        self.FRAMEWORK_REGISTRY
                        + kwargs.get("type")
                        + "/"
                        + kwargs.get("name"),
                        adaptors=True,
                    )
                else:
                    await self.install(
                        self.FRAMEWORK_REGISTRY
                        + kwargs.get("type")
                        + "/"
                        + kwargs.get("name")
                    )
            except Exception as e:
                return e
            if "path" not in list(kwargs.keys()):
                os.chdir("../")
            else:
                path = kwargs.get("path").split("/")
                for fr in path:
                    os.chdir("../")
            return ResponseCommand(
                response=f"{type} loaded sucessfully", process_status=True
            )
