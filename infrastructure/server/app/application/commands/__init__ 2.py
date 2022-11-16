"""cli command"""
import asyncio
import json
import os

import click
from adaptors.mongodb.mongoadaptor import DataBaseManager
from flask import Blueprint
from infrastructure.server.app.application.service import str_import
from infrastructure.shared_di.di import obj_graph

usersbp = Blueprint("load_data", __name__)


@usersbp.cli.command("create")
@click.argument("name")
def create(name):
    """loads data into database from json file"""
    os.chdir("fixture")
    os.chdir("AppFixtures")
    filesname = os.listdir(".")
    filesname = [x for x in filesname if x.startswith(name)]
    dab = obj_graph.provide(DataBaseManager)
    os.chdir("../..")
    file = open("dtos.json", "rb")
    file = json.loads(file.read())

    files = [
        {
            x.replace(".json", ""): str_import(
                ".".join(file[x.replace(".json", "")][0:-1]), x.replace(".json", "")
            )
        }
        for x in filesname
    ]
    for i in filesname:
        os.chdir("fixture")
        os.chdir("AppFixtures")
        data = json.load(open(i))
        cal = None
        for k in files:
            try:
                cal = k[i.replace(".json", "")]
            except KeyError as e:
                print("dto not found")
        if cal is not None:
            for x in data:
                nam = cal(**x)
                asyncio.run(dab.save(nam))
                print(f"record created:{nam.id}")


@usersbp.cli.command("dump")
@click.option("--name", "-n", multiple=True)
@click.argument("filepath")
def dump(name, filepath):
    """_summary_

    Args:
        name (_type_): _description_
        filepath (_type_): _description_
    """

    dab = obj_graph.provide(DataBaseManager)
    file = open("dtos.json", "rb")
    file = json.loads(file.read())

    files = [{"".join(x.split(",")): str_import(file[x][0], file[x][1])} for x in name]
    for x in name:
        data = None
        try:
            data = asyncio.run(
                dab.get_all(
                    *[
                        c["".join(x.split(","))]
                        for c in files
                        if c.get("".join(x.split(",")))
                    ]
                )
            )
        except KeyError as e:
            print("dto not found")
        if data is not None:
            with open(os.path.join(filepath, f"{x}.json"), "w+") as fas:
                das = []
                for i in data:
                    gah = i.dict()
                    del gah["id"]
                    das.append(gah)
                json.dump(das, fas)
