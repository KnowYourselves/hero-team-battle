# standard library
import math
import random

from collections import Counter

# others libraries
from pydantic import BaseModel
from pydantic import Field
from pydantic import PrivateAttr

# typing
from typing import Any


class APIConfig(BaseModel):
    base_url: str
    api_key: str


class Biography(BaseModel):
    full_name: str = Field(..., alias="full-name")
    alignment: str


class Powerstats(BaseModel):
    intelligence: int
    strength: int
    speed: int
    durability: int
    power: int
    combat: int
    actual_stamina: int = Field(default_factory=lambda: random.randint(0, 10))
    __filiation_coefficient: float = PrivateAttr(0)

    @property
    def filiation_coefficient(self) -> float:
        return self.__filiation_coefficient

    @filiation_coefficient.setter
    def filiation_coefficient(self, value: float) -> None:
        self.__filiation_coefficient = value


class Hero(BaseModel):
    hero_id: int = Field(..., alias="id")
    name: str
    biography: Biography
    powerstats: Powerstats
    __health_points: float = PrivateAttr(0)

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        self.__health_points = self.get_base_health_points()

    def get_base_health_points(self) -> float:
        stats_coef = (
            self.powerstats.strength * 0.8
            + self.powerstats.durability * 0.7
            + self.powerstats.power
        ) / 2
        actual_stamina_coef = 1 + self.powerstats.actual_stamina / 10
        return stats_coef * actual_stamina_coef + 100

    @property
    def health_points(self) -> float:
        return self.__health_points

    @health_points.setter
    def health_points(self, value: float) -> None:
        self.__health_points = min(0, self.__health_points, value)

    def reset_health_points(self) -> None:
        self.__health_points = self.get_base_health_points()

    @property
    def mental_attack(self) -> float:
        return (
            self.powerstats.intelligence * 0.8
            + self.powerstats.speed * 0.2
            + self.powerstats.combat * 0.1
        ) * self.powerstats.filiation_coefficient

    @property
    def strong_attack(self) -> float:
        return (
            self.powerstats.strength * 0.6
            + self.powerstats.power * 0.2
            + self.powerstats.combat * 0.2
        ) * self.powerstats.filiation_coefficient

    @property
    def fast_attack(self) -> float:
        return (
            self.powerstats.speed * 0.55
            + self.powerstats.durability * 0.25
            + self.powerstats.strength * 0.2
        ) * self.powerstats.filiation_coefficient

    def attack(self, other: "Hero") -> tuple[str, float]:
        attack_name, health_points_lost = self.get_random_attack()
        other.health_points -= health_points_lost
        return attack_name, health_points_lost

    def get_random_attack(self) -> tuple[str, float]:
        return random.choice(list(self.get_possible_attacks().items()))

    def get_possible_attacks(self) -> dict[str, float]:
        return {
            "mental_attack": self.mental_attack,
            "strong_attack": self.strong_attack,
            "fast_attack": self.fast_attack,
        }

    def get_filiation_coefficient(self, alignment: str) -> float:
        base = 1 + random.randint(0, 9)
        exponent = 1 if self.biography.alignment == alignment else -1
        return math.pow(base, exponent)


class HeroTeam(BaseModel):
    heroes: list[Hero] = Field(..., min_items=5, max_items=5, unique_items=True)

    @property
    def alignment(self) -> str:
        alignments = Counter([hero.biography.alignment for hero in self.heroes])
        alignment, _ = alignments.most_common(1)[0]
        return alignment

    def set_filiation_coefficient(self) -> None:
        for hero in self.heroes:
            hero.powerstats.filiation_coefficient = hero.get_filiation_coefficient(
                self.alignment
            )
