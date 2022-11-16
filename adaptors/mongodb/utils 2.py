"""mongodb motor and engine"""
import os

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorGridFSBucket
from odmantic import AIOEngine


class GridFSFile:
    """_summary_"""

    def __call__(self, conn: object):
        self.db = "test"
        return AsyncIOMotorGridFSBucket(getattr(conn, self.db))


class AsyncMoter:
    """_summary_"""

    def __call__(self, conn: str):
        return AsyncIOMotorClient(conn)


class AsyncEngine:
    """_summary_"""

    def __call__(self, motor_client: object, database: str):
        return AIOEngine(motor_client=motor_client, database=database)
