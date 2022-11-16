from typing import Dict
import os
import json
import pip
import asyncio


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

    async def install(self, package):
        if hasattr(pip, "main"):
            pip.main(["install", package])
        else:
            pip._internal.main(["install", package])

    async def format_config(self, **kwargs):
        with open("framework/framework_config.json", "rb") as fs:
            data = json.load(fs)
            fs.close()
            return data

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
        print(kwargs)
        return dict(error="type and from kwargs are required")

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
            return resp
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
            return resp

    async def from_(self, **kwargs):
        type = kwargs.get("type")
        if "from" in list(kwargs.keys()) and kwargs["from"] == "FRAMEWORK_REGISTRY":
            if "path" not in list(kwargs.keys()):
                os.chdir(kwargs.get("type"))
            else:
                os.chdir(kwargs.get("path"))
            try:
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
            return dict(response=f"{type} loaded sucessfully")
        elif "from" in list(kwargs.keys()) and kwargs["from"] == "GIT_URL":
            if "path" not in list(kwargs.keys()):
                os.chdir(kwargs.get("type"))
            else:
                os.chdir(kwargs.get("path"))
            try:
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
            return dict(response=f"{type} loaded sucessfully")
