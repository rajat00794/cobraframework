import os
import asyncio


async def setup_project_with_user():
    os.environ["FLASK_APP"] = os.getenv("App_Path")
    data = os.system("flask load_data create Permission")
    print(data)
    data = os.system("flask load_data create Role")
    print(data)
    from adaptors.mongodb.mongoadaptor import DataBaseManager
    from infrastructure.shared_di.di import obj_graph
    from modules.user.business.dtos.permission import Permission
    from modules.user.business.dtos.role import Role

    db = obj_graph.provide(DataBaseManager)
    permissions = await db.get_all(Permission)
    permissions = [str(x.id) for x in permissions]
    roles = await db.get_all(Role)
    roles = [str(x.id) for x in roles]
    for i in roles:
        data = await db.update_one(Role, dict(id=i), dict(permissions=permissions))
        print(f"done {i}", data)
    return True


setup = asyncio.run(setup_project_with_user())

if setup:
    print(type(setup), setup)
    print(
        "==========================Project setup sucessfully==========================="
    )
else:
    print(type(setup), setup, "rfr")
    print(
        "===========================something went wrong:-connect empty db -run again================================"
    )
