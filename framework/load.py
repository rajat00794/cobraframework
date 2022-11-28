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

    async def load_from_configfile(self):
        """_summary_"""
        with open("config.json", "rb") as fs:
            data = json.load(fs)
        for k, v in data.items():
            if k == "appwiseconfig":
                for h, j in v.items():
                    if h == "appconfig":
                        for p in j:
                            await self.load_application(**p)
            else:
                for tr in v:
                    await self.modules(**tr)

    async def install(self, package):
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
                dirsdd = None
                if "/" in dirs[-1]:
                    print(dirs[-1])
                    dirsdd = dirs[-1].split("/")[0]
                else:
                    dirsdd = dirs[0]
                os.chdir(os.getenv("APPROOT"))
                with open(".framework.json", "rb") as fd:
                    der = json.loads(fd.read())
                if dirsdd == "infrastructure":
                    dirsdd = "app"
                for j in der:
                    if j["type"] == dirsdd:
                        fs.writelines(j["init"].format(dirsd))
                fd.close()
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
            "type" in list(kwargs["config"].keys())
            and kwargs["config"]["type"] == "modules"
            or kwargs["config"]["type"] == "adaptors"
        ):
            return await self.modules(**kwargs)
        elif "type" in list(kwargs["config"].keys()) and kwargs["config"]["type"] == "common_utilities":
            return await self.modules(**kwargs)
        elif "type" in list(kwargs["config"].keys()) and kwargs["config"]["type"] == "application":
            return await self.load_application(**kwargs)
        return ResponseCommand(
            response="type and from kwargs are required", process_status=False
        )

    async def modules(self, **kwargs):
        """_summary_

        Returns:
            _type_: _description_
        """
        print(kwargs)
        for k, v in kwargs.items():
            if k == "config":
                data = await self.from_(**v)
                return ResponseCommand(response=str(data), process_status=True)

    async def load_app_config(self, app_config: dict):
        """_summary_

        Args:
            app_config (dict): _description_

        Returns:
            _type_: _description_
        """
        final = []
        for io in [app_config["dependency_modules"], app_config["dependency_adaptors"]]:
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
                            await self.install(url_subpackage)
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
        name = kwargs.get("appname")
        Approot = os.getenv("APPROOT")
        Appath = os.getenv("Apppath")
        url = self.FRAMEWORK_REGISTRY + f"{Appath}/{name}"
        await self.load_app_config(kwargs.get("config"))
        os.chdir(Approot)
        os.chdir(Appath)
        await self.install(url)
        return ResponseCommand(response="app loaded", process_status=True)

    async def from_(self, **kwargs):
        """_summary_

        Returns:
            _type_: _description_
        """
        type = kwargs.get("type")
        if "from" in list(kwargs.keys()) and kwargs["from"] == "FRAMEWORK_REGISTRY":
            if "path" not in list(kwargs.keys()):
                print(os.listdir("."))
                os.chdir(os.getenv("APPROOT"))
                os.chdir(kwargs.get("type"))
            else:
                os.chdir(os.getenv("APPROOT"))
                os.chdir(kwargs.get("path"))
            try:
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
