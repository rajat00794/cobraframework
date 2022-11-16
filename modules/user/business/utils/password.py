from passlib.hash import bcrypt_sha256 as bcrypt


class Password:
    def hash_pass(self, password):
        """_summary_

        Args:
            password (_type_): _description_

        Returns:
            _type_: _description_
        """
        return bcrypt.hash(password.encode("utf8"))

    def check_pass(self, password, hash):
        """_summary_

        Args:
            password (_type_): _description_
            hash (bool): _description_

        Returns:
            _type_: _description_
        """
        if not password or not hash:
            return "no password provided"
        if bcrypt.verify(password.encode("utf-8"), hash.encode("utf-8")):
            return password
        else:
            return "password not matched"
