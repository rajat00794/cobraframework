import os


class Config:
    API_KEY = os.getenv("api_key")
    SMS_URL = os.getenv("sms_url")

    def get_sms_uri(self):
        return dict(url=self.SMS_URL, api_key=self.API_KEY)
