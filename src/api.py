# standard library
import os

# others libraries
import requests

from src.models import Hero
from src.settings import settings


class SuperheroAPI:
    def get_hero(self, hero_id: int) -> Hero:
        full_url = self.get_full_url(hero_id)
        data = requests.get(full_url).json()
        return Hero.parse_obj(data)

    @staticmethod
    def get_full_url(hero_id: int) -> str:
        return os.path.join(
            settings.hero_base_url,
            "api",
            settings.hero_api_key,
            str(hero_id),
        )
