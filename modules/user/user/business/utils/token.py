import jwt
import os
from datetime import datetime, timedelta


class Token:
    secret_key = os.getenv("SECRET_KEY")

    def generate_acess_token(self, payload):
        dt = datetime.now() + timedelta(days=2)
        payload["exp"] = dt
        encoded = jwt.encode(payload, self.secret_key, algorithm="HS256")
        return encoded

    def decode_token(self, token):
        jwt_options = {"verify_aud": False, "require_sub": True}

        return jwt.decode(
            token, self.secret_key, algorithms=["HS256"], jwt_options=jwt_options
        )

    def generate_auth_tokens(self, payload):
        ref = payload
        dt = datetime.now() + timedelta(days=7)
        ref["exp"] = dt
        return dict(
            access_token=self.generate_acess_token(payload),
            refresh_token=self.generate_acess_token(ref),
        )

    def from_refresh_token(self, token):
        payload = self.decode_token(token)
        return self.generate_auth_tokens(payload)
