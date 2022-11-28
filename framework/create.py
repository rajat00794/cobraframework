import os
import json
from framework.configtemplates.templateschemaloader import Template


class CreateComponents:
    """_summary_"""

    def file_writer(self, dataq):
        if hasattr(dataq, "initfiles"):
            dataq = getattr(dataq, "initfiles")
        else:
            dataq = dataq
        for i in dataq:
            with open(i.filename, "w") as ds:
                for ui in i.content:
                    ds.writelines(ui)
                ds.close()
        return True

    def create_new(self, **kwargs):
        """_summary_"""
        if "type" in kwargs.keys():
            config = Template(name=kwargs["name"], type=kwargs["type"])
            config = config.get_config_instances()[0]
            if config.initfolders == []:
                os.chdir(os.getenv("APPROOT"))
                if config.type != "app":
                    os.chdir(config.type)
                    os.makedirs(config.name, exist_ok=True)
                    os.chdir(config.name)
                    if self.file_writer(config):
                        return kwargs["type"] + "loaded", 200
                else:
                    os.chdir(os.getenv("APPPATH"))
                    os.makedirs(kwargs["name"], exist_ok=True)
                    os.chdir(config.name)
                    if self.file_writer(config):
                        return kwargs["type"] + "loaded", 200
            else:
                os.chdir(os.getenv("APPROOT"))
                os.chdir(config.type)
                os.makedirs(config.name, exist_ok=True)
                os.chdir(config.name)
                self.file_writer(config)
                for i in config.initfolders:
                    self.create_sub(i)
            self.update_config(config=config)
            return True

    def create_sub(self, config):
        os.makedirs(config.name, exist_ok=True)
        os.chdir(config.name)
        self.file_writer(config.files)
        sub = config.subfolders
        if sub == [] or sub is None:
            return "create initfolders"
        else:
            return list(map(self.create_sub, sub))

    def update_config(self, **kwargs):
        """_summary_"""
        os.chdir(os.getenv("APPROOT"))
        with open("config.json", "rb") as fs:
            data = json.load(fs)
        for i in list(data.keys()):
            form = None
            if i.startswith(kwargs["config"].type):
                for u, hy in enumerate(data[i]):
                    form = data[i][u]
                    for io in list(form.keys()):
                        if io.startswith(kwargs["config"].type):
                            name = "".join([kwargs["config"].type, "name"])
                            form[name] = kwargs["config"].name
                            form["config"]["type"] = kwargs["config"].type
                            form["config"]["from"] = "LOCAL"
                            form["dependency_common_utilities"] = []
                            if os.getenv("ADAPTORSPATH") and form["adaptors_path"]:
                                form["adaptors_path"] = os.getenv("ADAPTORSPATH")
            if form is not None:
                print("all good")
                data[i].append(form)
            else:
                print("==========processing.===========")
            with open("config.json", "w") as fid:
                json.dump(data, fid)
            fs.close()
            fid.close()
        return True
