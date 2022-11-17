"""db config"""
import os
from typing import Optional


class Config:
    """_summary_

    Returns:
        _type_: _description_
    """

    user: str
    password: str
    host: str
    port: Optional[int] = 0
    dbname: str
    driver: str

    def __init__(self) -> None:
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("PASSWORD")
        self.host = os.getenv("HOST")
        self.port = os.getenv("PORT")
        self.dbname = os.getenv("DBNAME")
        self.driver = os.getenv("DRIVER")

    def get_uri(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if int(self.port) == 0:
            if self.dbname == str(None):
                return f"{self.driver}://{self.user}:{self.password}@{self.host}/?ssl=true&ssl_cert_reqs=CERT_NONE"
            return f"{self.driver}://{self.user}:{self.password}@{self.host}/{self.dbname}/?ssl=true&ssl_cert_reqs=CERT_NONE"

        elif self.dbname == str(None):
            return (
                f"{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}"
            )
        return f"{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}"
