from __future__ import annotations

from src.models import Hero
from src.models import HeroTeam


class TeamBattleLog:
    def __init__(self, team_alpha: HeroTeam, team_beta: HeroTeam) -> None:
        self.team_alpha = team_alpha
        self.team_beta = team_beta
        self.battle_logs: list[BattleLog] = []
        self.winner: HeroTeam | None = None

    def log_battle(self, hero_alpha: Hero, hero_beta: Hero) -> BattleLog:
        battle_log = BattleLog(hero_alpha, hero_beta)
        self.battle_logs.append(battle_log)
        return battle_log

    def log_winner(self, winner: HeroTeam) -> None:
        self.winner = winner


class BattleLog:
    def __init__(self, hero_alpha: Hero, hero_beta: Hero) -> None:
        self.hero_alpha = hero_alpha
        self.hero_beta = hero_beta
        self.attack_logs: list[AttackLog] = []
        self.winner: Hero | None = None

    def log_attack(
        self,
        attacker: Hero,
        attack_name: str,
        health_points: float,
    ) -> AttackLog:
        attacker, defender = self.get_attacker_and_defender(attacker)
        attack_log = AttackLog(attacker, defender, attack_name, health_points)
        self.attack_logs.append(attack_log)
        return attack_log

    def get_attacker_and_defender(self, attacker: Hero) -> tuple[Hero, Hero]:
        if attacker == self.hero_alpha:
            return (self.hero_alpha, self.hero_beta)
        return (self.hero_beta, self.hero_alpha)

    def log_winner(self, winner: Hero) -> None:
        self.winner = winner


class AttackLog:
    def __init__(
        self, attacker: Hero, defender: Hero, attack_name: str, health_points: float
    ) -> None:
        self.attacker = attacker
        self.defender = defender
        self.attack_name = attack_name
        self.health_points = health_points
