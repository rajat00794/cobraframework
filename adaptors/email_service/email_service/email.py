import asyncio
import aiosmtplib
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from adaptors.email_service.emailconfig import Config


class EmailUtils:
    def mimemultipart(self):
        return MIMEMultipart()

    def mimetext(self, text, textType, encode="utf-8"):
        return MIMEText(text, textType, encode)

    def config(self):
        return Config

    def aiostmp(self):
        return aiosmtplib


class EmailMessage:
    async def __init__(self, emailutils: object) -> None:
        self.utils = emailutils

    async def send_mail_async(self, to, subject, text, textType="plain", **params):
        """_summary_

        Args:
            to (_type_): _description_
            subject (_type_): _description_
            text (_type_): _description_
            textType (str, optional): _description_. Defaults to 'plain'.

        Returns:
            _type_: _description_
        """
        cc = params.get("cc", [])
        bcc = params.get("bcc", [])
        mail_params = params.get("mail_params", self.utils.config().get_parms())
        msg = self.utils.mimemultipart()
        msg.preamble = subject
        msg["Subject"] = subject
        msg["From"] = self.utils.config().get_parms()["user"]
        msg["To"] = ", ".join(to)
        if len(cc):
            msg["Cc"] = ", ".join(cc)
        if len(bcc):
            msg["Bcc"] = ", ".join(bcc)
        msg.attach(self.utils.mimetext(text, textType, "utf-8"))
        host = mail_params.get("host", "localhost")
        isSSL = mail_params.get("SSL", False)
        isTLS = mail_params.get("TLS", False)
        port = mail_params.get("port", 465 if isSSL else 25)
        smtp = self.utils.aiostmp().SMTP(hostname=host, port=port, use_tls=isSSL)
        await smtp.connect()
        res = []
        if isTLS:
            await smtp.starttls()
        if "user" in mail_params:
            await smtp.login(mail_params["user"], mail_params["password"])
            data = await smtp.send_message(msg)
            res.append(data)
        await smtp.quit()
        return res
