# standard library
import os

# others libraries
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class Settings(BaseModel):
    team_size: int
    hero_amount: int
    hero_base_url: str
    hero_api_key: str
    mailgun_api_key: str
    mailgun_base_url: str
    mailgun_sender: str
    email_destination: str


settings = Settings(
    team_size=int(os.environ.get("TEAM_SIZE", 5)),
    hero_amount=int(os.environ.get("HERO_AMOUNT", 731)),
    hero_base_url=os.environ.get("SUPERHERO_API_BASE_URL", ""),
    hero_api_key=os.environ.get("SUPERHERO_API_KEY", ""),
    mailgun_api_key=os.environ.get("MAILGUN_API_KEY", ""),
    mailgun_base_url=os.environ.get("MAILGUN_API_BASE_URL", ""),
    mailgun_sender=os.environ.get("MAILGUN_SENDER", ""),
    email_destination=os.environ.get("EMAIL_DESTINATION", ""),
)
