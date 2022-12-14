# standard library
import random

from src.models import Hero
from src.models import HeroTeam
from src.team_battle_log import BattleLog
from src.team_battle_log import TeamBattleLog
from src.team_builder import TeamBuilder


class TeamBattle:
    def __init__(self) -> None:
        self.team_builder = TeamBuilder()
        self.team_alpha = self.build_team()
        self.team_beta = self.build_team()
        self.team_battle_log = TeamBattleLog(self.team_alpha, self.team_beta)

    def build_team(self) -> HeroTeam:
        print("Building team...", end="", flush=True)
        team = self.team_builder.build_random_team()
        print(" Done!")
        return team

    def battle(self) -> None:
        print(f"{self.team_alpha} V/S {self.team_beta}\n")

        while self.team_alpha.active_hero and self.team_beta.active_hero:
            winner = self.hero_fight(
                self.team_alpha.active_hero,
                self.team_beta.active_hero,
            )
            winner.reset_health_points()

        winner_team = self.team_alpha if self.team_alpha.active_hero else self.team_beta
        print(f"Winner is {winner_team}!")

        print("Sending report...", end="", flush=True)
        self.team_battle_log.log_winner(winner_team)
        self.team_battle_log.send_report()
        print(" Done!")

    def hero_fight(self, hero_alpha: Hero, hero_beta: Hero) -> Hero:
        print(f"\t{hero_alpha} V/S {hero_beta}")

        battle_log = self.team_battle_log.log_battle(hero_alpha, hero_beta)
        heroes = [hero_alpha, hero_beta]
        current_hero_index = random.randint(0, 1)
        while hero_alpha.health_points > 0 and hero_beta.health_points > 0:
            self.hero_attack(heroes, current_hero_index, battle_log)
            current_hero_index = (1 + current_hero_index) % 2
        winner = heroes[0] if heroes[0].health_points > 0 else heroes[1]
        winner_team = self.get_team_from_hero(winner)
        battle_log.log_winner(winner, winner_team)

        print(f"\tWinner is {winner} from {winner_team}!\n")
        return winner

    def hero_attack(
        self, heroes: list[Hero], current_hero_index: int, battle_log: BattleLog
    ) -> None:
        attacker = heroes[current_hero_index]
        defender = heroes[1 - current_hero_index]
        attack_name, health_points = attacker.attack(defender)
        battle_log.log_attack(attacker, attack_name, health_points)
        print(
            f"\t\t{attacker} uses {attack_name} and {defender} loses "
            f"{health_points} health points!"
        )

    def get_team_from_hero(self, hero: Hero) -> HeroTeam:
        if hero == self.team_alpha.active_hero:
            return self.team_alpha
        return self.team_beta
