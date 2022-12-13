# standard library
import random

# others libraries
from pydantic import ValidationError

from src.api import SuperheroAPI
from src.models import Hero
from src.models import HeroTeam


class TeamBuilder:
    def __init__(self) -> None:
        self.api = SuperheroAPI()

    def build_random_team(self) -> HeroTeam:
        heroes = self.get_five_random_heroes()
        team = HeroTeam(heroes=heroes)
        team.set_filiation_coefficient()
        return team

    def get_five_random_heroes(self) -> list[Hero]:
        heroes: list[Hero] = []
        excluded: set[int] = set()
        while len(heroes) < 5:
            hero_id = self.get_random_hero_id(excluded)
            if hero_id in excluded:
                continue

            hero = self.get_hero(hero_id)
            if hero:
                heroes.append(hero)
        return heroes

    def get_hero(self, hero_id: int) -> Hero | None:
        try:
            return self.api.get_hero(hero_id)
        except ValidationError:
            return None

    @staticmethod
    def get_random_hero_id(excluded: set[int]) -> int:
        options = [hero_id for hero_id in range(1, 732) if hero_id not in excluded]
        return random.choice(options)
