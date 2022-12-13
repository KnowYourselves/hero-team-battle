# others libraries
from dotenv import load_dotenv

from src.team_battle import TeamBattle

if __name__ == "__main__":
    load_dotenv()
    battle = TeamBattle()
    battle.battle()
