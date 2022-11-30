from flask_openapi3 import APIBlueprint,Tag,Info
from typing import List,Callable,Optional,Any




class Cobraframeworkutils:
    type_="cobra"
    def view_const(self)->function:
        route:callable(object,[object,{}]) = lambda x,y:getattr(y[0],y[1]["service"])(**y[1]["vars"])
        return route

    def assembly_(self,x):
        user_tag = Tag(name=x.__class__.__name__, description="test")
        bp=APIBlueprint(f"/{x.apiprifix}", __name__, url_prefix=x.apiprifix, abp_tags=[user_tag], doc_ui=True)
        methods=[getattr(x,m) for m in dir(x) if not m.startswith('__')]
        for i in methods:
            i=getattr(bp,*[x.lower() for x in i.__defaults__ if x in ["GET","POST","PUT","DELETE","PATCH"]])(self.view_const()())
        return methods

    def create_routes(self,services:List[object]):
        info = Info(title="Test API", version="1.0.0")
        services_list=map(lambda x:x,list(map(lambda x:x if hasattr(x,"apiprifix") else setattr(x,"apiprifix",x.__class__.__name__),services)))
        
