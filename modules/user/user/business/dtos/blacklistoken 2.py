"""blacklist token model"""
from odmantic import Model


class BlacklistToken(Model):
    """_summary_

    Args:
        Model (_type_): _description_
    """

    token: str
    unique_fields: list = []
