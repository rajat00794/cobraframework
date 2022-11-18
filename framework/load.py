from typing import Dict
import os
import json
import pip
import asyncio
import importlib
from pydantic import BaseModel
from pprint import pprint


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
        """_summary_"""
        if os.getenv("FRAMEWORK_REGISTRY") is not None:
            self.FRAMEWORK_REGISTRY = os.getenv("FRAMEWORK_REGISTRY")
        else:
            self.FRAMEWORK_REGISTRY = asyncio.run(self.format_config())[
                "FRAMEWORK_REGISTRY"
            ]

    async def install(self, package, app=None, adaptors=None, common_utilities=None):
        """_summary_

        Args:
            package (_type_): _description_
            app (_type_, optional): _description_. Defaults to None.
            adaptors (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        if hasattr(pip, "main"):
            pip.main(["install", package])
            dirs = package.split("=")
            dirsd = None
            if "/" in dirs[-1]:
                dirsd = dirs[-1].split("/")[-1]
            else:
                dirsd = dirs[-1]
            os.makedirs(dirsd, exist_ok=True)
            os.chdir(dirsd)
            with open("__init__.py", "w+") as fs:
                if app is None and adaptors is None and common_utilities is None:
                    fs.writelines(f"from {dirsd} import business,enterprise")
                elif app is not None:
                    fs.writelines(f"from {dirsd} import routes")
                elif adaptors is not None:
                    fs.writelines(f"import {dirsd}")
                elif common_utilities is not None:
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
        """_summary_

        Returns:
            _type_: _description_
        """
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
        elif "type" in list(kwargs.keys()) and kwargs["type"] == "common_utilities":
            return await self.modules(common_utilities=True, **kwargs)
        elif "type" in list(kwargs.keys()) and kwargs["type"] == "application":
            return await self.load_application(**kwargs)
        return ResponseCommand(
            response="type and from kwargs are required", process_status=False
        )

    async def modules(self, common_utilities=None, **kwargs):
        """_summary_

        Returns:
            _type_: _description_
        """
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
            return ResponseCommand(response=resp.response, process_status=True)
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
        elif common_utilities is not None:
            if "path" not in list(kwargs.keys()):
                data = {
                    "from": kwargs.get("from"),
                    "name": "",
                    "type": kwargs.get("type"),
                }
            else:
                data = {
                    "from": kwargs.get("from"),
                    "name": "",
                    "type": kwargs.get("type"),
                    "path": kwargs.get("path"),
                }

            resp = await self.from_(common_utilities=True, **data)
        else:
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
            return ResponseCommand(response=resp.response, process_status=True)

    async def load_app_config(self, app_config: dict):
        """_summary_

        Args:
            app_config (dict): _description_

        Returns:
            _type_: _description_
        """
        final = []
        for io in [
            app_config["dependency_modules"],
            app_config["dependency_adaptors"],
            app_config["dependency_common_utilities"],
        ]:
            subpackage = []
            for m in io:
                if type(m) != bool:
                    await self.load(**m[list(m.keys())[0]])
                    pprint(m[list(m.keys())[0]], depth=1)
                    print(
                        f"========={m[list(m.keys())[0]]['type']} loaded {m[list(m.keys())[0]]['name']}==========="
                    )
                    os.chdir("../")
                    subpackage.append(
                        {m[list(m.keys())[0]]["type"]: m[list(m.keys())[0]]["name"]}
                    )
                else:
                    for iy in app_config["dependency_common_utilities"]:
                        if iy:
                            url_subpackage = (
                                self.FRAMEWORK_REGISTRY + f"common_utilities"
                            )
                            await self.install(url_subpackage, common_utilities=True)
                            os.chdir("../")
                            subpackage.append({"common_utilities": True})
                        else:
                            pass
            final.append(subpackage)

        return ResponseCommand(response=str(final), process_status=True)

    async def load_application(self, **kwargs):
        """_summary_

        Returns:
            _type_: _description_
        """
        if "from" in list(kwargs.keys()) and kwargs["from"] == "FRAMEWORK_REGISTRY":
            with open("config.json", "rb") as fs:
                data = json.load(fs)
            name = kwargs.get("name")
            url = (
                self.FRAMEWORK_REGISTRY
                + f"infrastructure/server/app/application/{name}"
            )
            app_config = map(
                self.load_app_config,
                [
                    x["config"]
                    for x in data["appconfig"]
                    if x["appname"] == kwargs.get("name")
                ],
            )
            pprint([await x for x in list(app_config)])
            os.chdir(data["app_root"])
            os.chdir(data["app_path"])
            await self.install(url, app=True)
            return ResponseCommand(response="app loaded", process_status=True)

    async def from_(self, common_utilities=None, **kwargs):
        """_summary_

        Returns:
            _type_: _description_
        """
        type = kwargs.get("type")
        if "from" in list(kwargs.keys()) and kwargs["from"] == "FRAMEWORK_REGISTRY":
            if "path" not in list(kwargs.keys()):
                print(os.listdir("."))
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
                elif common_utilities is not None:
                    await self.install(self.FRAMEWORK_REGISTRY+ kwargs.get("type")
                        ,common_utilities=True,
                    )
                else:
                    await self.install(
                        self.FRAMEWORK_REGISTRY
                        + kwargs.get("type")
                        + "/"
                        + kwargs.get("name")
                    )
            except Exception as e:
                return ResponseCommand(response=str(e), process_status=False)
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
