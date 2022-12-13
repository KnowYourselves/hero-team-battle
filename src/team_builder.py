# standard library
import random

# others libraries
from pydantic import ValidationError

from src.api import SuperheroAPI
from src.models import Hero
from src.models import HeroTeam

TEAM_NAMES = (
    "Colo-Colo",
    "Universidad de Chile",
    "Universidad Católica",
    "Cobreloa",
    "Palestino",
    "Santiago Wanderers",
    "Tricolor de Paine",
)


class TeamBuilder:
    def __init__(self) -> None:
        self.api = SuperheroAPI()

    def build_random_team(self) -> HeroTeam:
        heroes = self.get_five_random_heroes()
        team = HeroTeam(name=random.choice(TEAM_NAMES), heroes=heroes)
        team.set_filiation_coefficient()
        return team

    def get_five_random_heroes(self) -> list[Hero]:
        heroes: list[Hero] = []
        excluded: set[int] = set()
        for _ in range(5):
            hero = self.get_hero(excluded)
            heroes.append(hero)
        return heroes

    def get_hero(self, excluded: set[int]) -> Hero:
        while len(excluded) < 731:
            try:
                hero_id = self.get_random_hero_id(excluded)
                excluded.add(hero_id)
                return self.api.get_hero(hero_id)
            except ValidationError:
                continue
        raise ValueError("No more heroes to choose from")

    @staticmethod
    def get_random_hero_id(excluded: set[int]) -> int:
        options = [hero_id for hero_id in range(1, 732) if hero_id not in excluded]
        return random.choice(options)
