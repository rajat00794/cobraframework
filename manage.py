#!/usr/bin/python

import click
from typing import Dict
import json
from framework.load import LoadComponents
import asyncio


def formet_args(**kwargs):
    final_args = []
    for k, v in kwargs.items():
        if len(v) != 0:
            args = []
            for f in v:
                try:
                    f[list(f.keys())[0]] = json.loads(f[list(f.keys())[0]])
                    args.append(f)
                except Exception as e:
                    click.echo(
                        f"args should be in string dict formet"
                        + '{"name":"someprojectname"}',
                        dict(error=e),
                    )
        final_args.append({k: args})
        args = []
    return final_args


@click.command()
@click.option("--load_module", default={})
@click.option("--load_application", default={})
@click.option("--load_apdaptor", default={})
@click.option("--deploy", default={})
@click.option("--load_project_config", default={})
@click.option("--create_project_config", default={})
@click.option("--load_common_utilities", default={})
@click.option("--generate_di", default={})
@click.option("--generate_microservises", default={})
@click.option("--create_modules", default={})
@click.option("--create_application", default={})
@click.option("--create_apdaptor", default={})
@click.option("--create_deployment_config", default={})
@click.option("--generate_project_config", default={})
def framework_commands(
    load_module={},
    load_application={},
    load_apdaptor={},
    deploy={},
    load_project_config={},
    create_project_config={},
    load_common_utilities={},
    generate_di={},
    generate_microservises={},
    create_modules={},
    create_application={},
    create_apdaptor={},
    create_deployment_config={},
    generate_project_config={},
):
    load = [
        dict(load_module=load_module),
        dict(load_application=load_application),
        dict(load_apdaptor=load_apdaptor),
        dict(load_project_config=load_project_config),
        dict(load_common_utilities=load_common_utilities),
    ]
    create = [
        dict(create_project_config=create_project_config),
        dict(create_modules=create_modules),
        dict(create_application=create_application),
        dict(create_apdaptor=create_apdaptor),
        dict(create_deployment_config=create_deployment_config),
    ]
    generator = [
        dict(generate_di=generate_di),
        dict(generate_microservises=generate_microservises),
        dict(generate_project_config=generate_project_config),
    ]
    deployment = [dict(deploy=deploy)]
    load = [x for x in load if x[list(x.keys())[0]] != "{}"]
    create = [x for x in create if x[list(x.keys())[0]] != "{}"]
    generator = [x for x in generator if x[list(x.keys())[0]] != "{}"]
    deployment = [x for x in deployment if x[list(x.keys())[0]] != "{}"]
    formateded_args = formet_args(
        load=load, create=create, generator=generator, deployment=deployment
    )
    formateded_args = [x for x in formateded_args if x[list(x.keys())[0]] != []]
    for io in formateded_args:
        if "load" in io.keys():
            gross_args = io["load"]
            for iu in gross_args:
                for iw in iu.keys():
                    if iw.startswith("load"):
                        loadm = LoadComponents()
                        asyncio.run(loadm.load(**iu[iw]))
    click.echo(formateded_args)


if __name__ == "__main__":
    framework_commands()
