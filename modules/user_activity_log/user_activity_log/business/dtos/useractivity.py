from typing import List
from datetime import datetime
from odmantic import Model, Field


class UserActivity(Model):
    """_summary_

    Args:
        Model (_type_): _description_
    """

    user_id: str
    headers: str
    data: str
    ip_information: str
    log_time: datetime = datetime.now()
    unique_fields: list = []
