from infrastructure.shared_di.di import obj_graph
from adaptors.mongodb.mongoadaptor import DataBaseManager


async def test_di():
    obj = obj_graph.provide(DataBaseManager)
    assert isinstance(obj, DataBaseManager)
