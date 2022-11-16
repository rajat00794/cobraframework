from typing import List, Any
from datetime import datetime
from pydantic import BaseModel


class ResponseActivity(BaseModel):
    """_summary_

    Args:
        Model (_type_): _description_
    """

    data: List[Any]
