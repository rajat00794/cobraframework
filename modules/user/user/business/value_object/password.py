"""password validator"""
import re
from xml.dom import ValidationErr


class Password:
    """_summary_

    Raises:
        ValidationErr: _description_

    Returns:
        _type_: _description_
    """

    regex: str = (
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    )

    def __init__(self, password: str) -> None:
        """_summary_

        Args:
            password (str): _description_

        Raises:
            ValidationErr: _description_

        Returns:
            _type_: _description_
        """
        self.com = re.compile(self.regex)
        if re.fullmatch(self.com, password):
            return password
        else:
            raise ValidationErr("password not valid")
