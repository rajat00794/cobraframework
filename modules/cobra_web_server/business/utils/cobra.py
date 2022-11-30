from flask_openapi3 import APIBlueprint, Tag, Info
from flask import request
from typing import Dict, List, Callable, Optional, Any
from pydantic import BaseModel
import os
import json
import importlib
from framework.generate import Generatecomponents


class Cobraframeworkutils:
    type_ = "cobra"
    obj_graph = Generatecomponents().generate_di()

    def view_const(self, config: Dict[str, Any] = {}) -> function:
        if config is not {}:
            if config.get("method") == "POST" and list(config.keys()) == [
                "method",
                "btype",
                "service",
                "service_method",
            ]:
                BODY_TYPE = config.get("btype")
                SERVICE = config.get("service")

                def route(body: BODY_TYPE, service: SERVICE = SERVICE):
                    service_obj = self.obj_graph.provide(service)
                    return getattr(service_obj, config.get("service_method"))(body)

            if config.get("method") == "PUT":
                BODY_TYPE = config.get("btype")
                SERVICE = config.get("service")
                PARMS = config.get("params")

                def route(path: PARMS, body: BODY_TYPE, service: SERVICE = SERVICE):
                    service_obj = self.obj_graph.provide(service)
                    return getattr(service_obj, config.get("service_method"))(
                        path, body
                    )

            if config["method"] == "PATCH":
                BODY_TYPE = config.get("btype")
                SERVICE = config.get("service")
                PARMS = config.get("params")

                def route(path: PARMS, body: BODY_TYPE, service: SERVICE = SERVICE):
                    service_obj = self.obj_graph.provide(service)
                    return getattr(service_obj, config.get("service_method"))(
                        path, body
                    )

            if config["method"] == "DELETE":
                BODY_TYPE = config.get("btype")
                SERVICE = config.get("service")
                PARMS = config.get("params")

                def route(path: PARMS, service: SERVICE = SERVICE):
                    service_obj = self.obj_graph.provide(service)
                    return getattr(service_obj, config.get("service_method"))(
                        path, BODY_TYPE
                    )

            if config["method"] == "GET":
                BODY_TYPE = config.get("btype")
                SERVICE = config.get("service")

                def route(service: SERVICE = SERVICE):
                    service_obj = self.obj_graph.provide(service)
                    return getattr(service_obj, config.get("service_method"))(
                        BODY_TYPE,
                        query_params=request.query_string
                        if request.query_string
                        else False,
                    )

            route.__name__ = config.get("service_method") + config["method"]
        return route

    def import_dto(self, name: str):
        with open("dtos.json", "rb") as fs:
            data = json.loads(fs)
        if name in list(data.keys()):
            module = importlib.import_module(data.get(name)[0])
            getattr(module, name)
            return module
        else:
            raise Exception("dto not found")

    def assembly(self, x):
        user_tag = Tag(name=x.__class__.__name__, description="test")
        bp = APIBlueprint(
            f"/{x.apiprifix}",
            __name__,
            url_prefix=x.apiprifix,
            abp_tags=[user_tag],
            doc_ui=True,
        )
        methods = [m for m in dir(x) if not m.startswith("__")]
        for i in methods:
            z = i
            i = getattr(x, i)
            getattr(
                bp,
                *[
                    x.lower()
                    for x in i.__defaults__
                    if x in ["GET", "POST", "PUT", "DELETE", "PATCH"]
                ],
            )(
                self.view_const(
                    config=dict(
                        btype=self.import_dto(
                            *[x for x in i.__defaults__ if type(x) == object]
                        ),
                        service=x,
                        method=[
                            x
                            for x in i.__defaults__
                            if x in ["GET", "POST", "PUT", "DELETE", "PATCH"]
                        ][0],
                        service_method=z,
                        query_params=True,
                        params=[
                            x
                            for x in i.__defaults__
                            if isinstance(x, list) and len(x) is not 0
                        ]
                        if [
                            x
                            for x in i.__defaults__
                            if isinstance(x, list) and len(x) is not 0
                        ]
                        != []
                        else [],
                    )
                ),
                f"{z}/"
                + "/".join(
                    [
                        f"<{x}>"
                        for x in i.__defaults__
                        if isinstance(x, list) and len(x) is not 0
                    ]
                ),
                responses={
                    "201": self.import_dto(
                        *[x for x in i.__defaults__ if type(x) == object]
                    )
                },
                description="test",
            )
        return bp

    def create_routes(self, services: List[object]):
        appname = os.getenv("API_TITLE")
        if appname:
            info = Info(title=f"{appname}", version="1.0.0")
        else:
            info = Info(title=f"TestApi", version="1.0.0")
        services_list = map(
            lambda x: self.assembly(x),
            list(
                map(
                    lambda x: x
                    if hasattr(x, "apiprifix")
                    else setattr(x, "apiprifix", x.__class__.__name__),
                    services,
                )
            ),
        )
        return list(services_list)
