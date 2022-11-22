import os
import json


class CreateComponents:
    """_summary_"""

    def create_new(self, **kwargs):
        """_summary_"""
        if "type" in kwargs.keys():
            if kwargs["type"] != "app":
                os.chdir(os.getenv("APPROOT"))
                os.chdir(kwargs["type"])
                os.makedirs(kwargs["name"], exist_ok=True)
                os.chdir(kwargs["name"])
                if kwargs["type"].startswith("adaptors"):
                    de = os.getenv("APPROOT")
                    with open(
                        f"{de}/framework/configtemplates/adaptors.json", "rb"
                    ) as fs:
                        dataq = json.loads(fs.read())
                    print(dataq)
                    for i in dataq:
                        print(type(i), "rfrfrfr")
                        for k, v in i.items():
                            if k == "initfiles":
                                for h in v:
                                    with open(
                                        list(h.keys())[0].format(kwargs["name"]), "w"
                                    ) as ds:
                                        for ui in list(h.values()):
                                            print(ui)
                                            map(ds.writelines, ui)
                                        ds.close()

            else:
                os.chdir(os.getenv("APPROOT"))
                os.chdir(os.getenv("APPPATH"))
                os.makedirs(kwargs["name"])

    def create_from_config(self, **kwargs):
        """_summary_"""
        pass

    def check_config_dir(self):
        """_summary_"""
        pass

    def update_config(self, **kwargs):
        """_summary_"""
        pass
