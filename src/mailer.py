# others libraries
import requests

from src.settings import settings


class Mailer:
    @staticmethod
    def send(email: str, subject: str, plain_text: str, html: str) -> requests.Response:
        return requests.post(
            settings.mailgun_base_url,
            auth=("api", settings.mailgun_api_key),
            data={
                "from": settings.mailgun_sender,
                "to": email,
                "subject": subject,
                "text": plain_text,
                "html": html,
            },
        )
