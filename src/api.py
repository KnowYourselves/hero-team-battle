# standard library
import os

# others libraries
import requests

from src.models import APIConfig
from src.models import Hero


class SuperheroAPI:
    def __init__(self) -> None:
        self.config = APIConfig(
            api_key=os.environ["SUPERHERO_API_KEY"],
            base_url=os.environ["SUPERHERO_API_BASE_URL"],
        )

    def get_full_url(self, hero_id: int) -> str:
        return os.path.join(
            self.config.base_url,
            "api",
            self.config.api_key,
            str(hero_id),
        )

    def get_hero(self, hero_id: int) -> Hero:
        full_url = self.get_full_url(hero_id)
        data = requests.get(full_url).json()
        return Hero.parse_obj(data)
