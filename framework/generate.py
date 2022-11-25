import os
import importlib

class Generatecomponents:
    def generate_di(self,config:dict):
        pass

    def get_args(self,config:dict):
        pass

    def importmodule(self,path:str):
        return importlib.import_module(path)

    def get_row_args(self):
        adaptor_args=[]
        listd=os.listdir("adaptors/")
        adaptor_args=[self.importmodule(".".join(["adaptors",x,x])) for x in listd if x!="__pycache__" and x!="__init__.py" if os.path.join(f"adaptors/",x)]
        return adaptor_args