from __future__ import annotations

# standard library
import os

from src.mailer import Mailer
from src.models import Hero
from src.models import HeroTeam
from src.settings import settings


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

    def send_report(self) -> None:
        destination = settings.email_destination
        subject = f"Team Battle Report - {self.team_alpha} V/S {self.team_beta}"
        text = teamlog_to_text(self)
        html = teamlog_to_html(self)

        mailer = Mailer()
        mailer.send(destination, subject, text, html)


class BattleLog:
    def __init__(self, hero_alpha: Hero, hero_beta: Hero) -> None:
        self.hero_alpha = hero_alpha
        self.hero_beta = hero_beta
        self.attack_logs: list[AttackLog] = []
        self.winner: Hero | None = None
        self.winner_team: HeroTeam | None = None

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

    def log_winner(self, winner: Hero, winner_team: HeroTeam) -> None:
        self.winner = winner
        self.winner_team = winner_team


class AttackLog:
    def __init__(
        self, attacker: Hero, defender: Hero, attack_name: str, health_points: float
    ) -> None:
        self.attacker = attacker
        self.defender = defender
        self.attack_name = attack_name
        self.health_points = health_points


def teamlog_to_text(team_battle_log: TeamBattleLog) -> str:
    text = f"Team Battle Report, Winner {team_battle_log.winner}\n\n"
    for i, battle_log in enumerate(team_battle_log.battle_logs):
        text += (
            f"Battle {i + 1} - {battle_log.hero_alpha} V/S {battle_log.hero_beta}\n\n"
        )
        text += f"Winner: {battle_log.winner} from {battle_log.winner_team}\n\n"
        text += "Attack Logs:\n"
        for attack_log in battle_log.attack_logs:
            text += (
                f"\t{attack_log.attacker} used {attack_log.attack_name} on "
                f"{attack_log.defender} and inflicted {attack_log.health_points} damage"
            )
    return text


def teamlog_to_html(team_battle_log: TeamBattleLog) -> str:
    space = "&nbsp;"
    html = f"""
        <div>
            Team Battle Report, Winner <b>{team_battle_log.winner}</b>
        </div>
        <br>
    """
    for i, battle_log in enumerate(team_battle_log.battle_logs):
        html += f"""
            <div>
                Battle {i + 1}
                - <b>{battle_log.hero_alpha}</b> V/S <b>{battle_log.hero_beta}</b>
            </div>
        """
        html += f"""
            <div>
                Winner: <b>{battle_log.winner}</b> from {battle_log.winner_team}
            </div>
            <br>
        """
        html += "<div>Attack Logs:</div>"
        for attack_log in battle_log.attack_logs:
            html += f"""
                <div>
                    </p>
                        {space*4}{attack_log.attacker} used {attack_log.attack_name} on
                        {attack_log.defender} and inflicted {attack_log.health_points}
                        damage
                    </p>
                </div>
            """
        html += "<br><br>"

    return html
