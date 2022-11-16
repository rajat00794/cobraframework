import requests
import urllib.parse


class Smsservice:
    def __init__(self, smsconfig: object) -> None:
        self.config = smsconfig

    def send_msg(self, phone, msg):
        parms = self.config.get_sms_uri()
        api = parms["api_key"]
        payload = f"module=TRANS_SMS&apikey={api}&to={phone}&from=HEADER&templatename=teste&msg=DLT%204566"
        headers = {}
        data = requests.request("POST", parms["url"], headers=headers, data=payload)
        return data.text
