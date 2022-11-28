import os
import importlib
from typing import List, Tuple
import pinject


class Generatecomponents:
    kwargs = {}

    def configure(self, bind):
        if self.kwargs is not None:
            for k, v in self.kwargs.items():
                bind(k, to_class=v)

    def generate_di(self):
        config = self.get_row_args()
        config = self.get_args(config)
        data = {}
        for i in config:
            data[i[0]] = i[1]
        self.kwargs = data
        DISPEC = type(
            os.getenv("appname").upper(),
            (pinject.BindingSpec,),
            dict(kwargs=self.kwargs, configure=self.configure),
        )
        obj_graph = pinject.new_object_graph(binding_specs=[DISPEC()])
        return obj_graph

    def get_args(self, config: List[List[Tuple[str, object]]]):
        # check duplicate
        final_args = []
        [final_args.append(x) for i in config for x in i if x not in final_args]
        return final_args

    def importmodule(self, path: str):
        return importlib.import_module(path)

    def get_row_args(self):
        adaptor_args = []
        os.chdir(os.getenv("APPROOT"))
        listd = os.listdir("adaptors/")
        adaptor_args = [
            self.importmodule(".".join(["adaptors", x]))
            for x in listd
            if x != "__pycache__" and x != "__init__.py" and x != ".DS_Store"
            if os.path.join(f"adaptors/", x)
        ]
        listd = os.listdir("modules/")
        module_args = [
            self.importmodule(".".join(["modules", x]))
            for x in listd
            if x != "__pycache__" and x != "__init__.py" and x != ".DS_Store"
            if os.path.join(f"modules/", x)
        ]
        listd = os.listdir("common_utilities/")
        common_utility_args = [
            self.importmodule(".".join(["common_utilities", x]))
            for x in listd
            if x != "__pycache__" and x != "__init__.py" and x != ".DS_Store"
            if os.path.join(f"common_utilities/", x)
        ]
        all_args = adaptor_args + module_args + common_utility_args
        final_args = []
        for hy in all_args:
            if hasattr(hy, "di_args"):
                final_args.append(getattr(hy, "di_args"))
        return final_args
