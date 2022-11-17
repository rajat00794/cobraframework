import os


class Config:
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_TLS = os.getenv("MAIL_TLS")
    MAIL_SSL = os.getenv("MAIL_SSL")

    def get_parms(self):
        return {
            "TLS": self.MAIL_TLS,
            "host": self.MAIL_SERVER,
            "password": self.MAIL_PASSWORD,
            "user": self.MAIL_USERNAME,
            "port": self.MAIL_PORT,
        }
