from typing import List, Optional
from datetime import datetime
from odmantic import Model


class Otp(Model):
    """_summary_

    Args:
        Model (_type_): _description_
    """

    otp: int
    user_id: str
    created_at: datetime
    expire_time: Optional[int] = 300
    unique_fields: list = []
