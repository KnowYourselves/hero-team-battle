# standard library
import random

from src.models import Hero
from src.models import HeroTeam
from src.team_builder import TeamBuilder


class TeamBattle:
    def __init__(self) -> None:
        self.team_builder = TeamBuilder()
        self.team_alpha = self.build_team()
        self.team_betta = self.build_team()

    def build_team(self) -> HeroTeam:
        print("Building team...")
        return self.team_builder.build_random_team()

    def battle(self) -> None:
        current_alpha_hero = 0
        current_betta_hero = 0
        while current_alpha_hero < 5 and current_betta_hero < 5:
            alpha_hero = self.team_alpha.heroes[current_alpha_hero]
            beta_hero = self.team_betta.heroes[current_betta_hero]
            winner = self.hero_fight(alpha_hero, beta_hero)
            winner.reset_health_points()
            current_alpha_hero += 1 if winner == beta_hero else 0
            current_betta_hero += 1 if winner == alpha_hero else 0

    def hero_fight(self, hero_alpha: Hero, hero_betta: Hero) -> Hero:
        heroes = [hero_alpha, hero_betta]
        current_hero_index = random.randint(0, 1)
        print(hero_alpha, "v/s", hero_betta)
        while hero_alpha.health_points > 0 and hero_betta.health_points > 0:
            self.hero_attack(heroes, current_hero_index)
            current_hero_index = (1 + current_hero_index) % 2
        winner = heroes[0] if heroes[0].health_points > 0 else heroes[1]
        print(f"Winner is {winner}!")
        return winner

    def hero_attack(self, heroes: list[Hero], current_hero_index: int) -> None:
        attacker = heroes[current_hero_index]
        defender = heroes[1 - current_hero_index]
        attack_name, health_points = attacker.attack(defender)
        print(
            f"{attacker} uses {attack_name} and {defender} loses "
            f"{health_points} health points!"
        )
