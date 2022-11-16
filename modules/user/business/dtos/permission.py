"""primission model"""
from odmantic import Model, Field


class Permission(Model):
    """_summary_

    Args:
        Model (_type_): _description_
    """

    permissionname: str
    permissionview: str
    unique_fields: list = ["permissionname"]
