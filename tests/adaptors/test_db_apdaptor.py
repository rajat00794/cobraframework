from adaptors.mongodb.mongoadaptor import DataBaseManager
from infrastructure.shared_di.di import obj_graph
from modules.user.business.dtos.user import User


async def test_db_adaptor():
    db = obj_graph.provide(DataBaseManager)
    dto = User(
        firstname="jitendra",
        lastname="prateek",
        email="rajatm@thoughtwin.com",
        password="Rajat322",
        phone="8160201174",
        role="636f3eda26e850e666e852b1",
    )
    data = await db.save(dto)
    assert data == dto
    await db.delete_one(User, dict(id=dto.id))
    assert 1 == 1
