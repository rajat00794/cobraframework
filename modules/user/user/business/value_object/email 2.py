"""email validator"""
import re
from xml.dom import ValidationErr


class Email:
    """_summary_

    Raises:
        ValidationErr: _description_

    Returns:
        _type_: _description_
    """

    regex: str = r"^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"

    def __init__(self, email: str) -> None:
        """_summary_

        Args:
            email (str): _description_

        Raises:
            ValidationErr: _description_

        Returns:
            _type_: _description_
        """
        self.com = re.compile(self.regex)
        if re.fullmatch(self.com, email):
            return email
        else:
            raise ValidationErr("email not valid")
