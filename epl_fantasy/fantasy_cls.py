from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class FirstRoundInfo:
    wins: int
    draws: int
    losses: int
    points_scored: int


@dataclass
class Team:
    player_name: str
    team_name: str
    first_round_info: FirstRoundInfo


@dataclass
class Fixture:
    home_team: Tuple[Team, Optional[int]]
    away_team: Tuple[Team, Optional[int]]


@dataclass
class Gameweek:
    number: int
    fixtures: List[Fixture]


@dataclass
class TeamStandingInfo:
    team: Team
    wins: int = None
    draws: int = None
    losses: int = None
    points: int = None
    points_scored: int = None

    def __post_init__(self):
        self.wins = self.team.first_round_info.wins
        self.draws = self.team.first_round_info.draws
        self.losses = self.team.first_round_info.losses
        self.points_scored = self.team.first_round_info.points_scored
        self.points = self.wins * 3 + self.draws * 1


@dataclass
class Standing:
    most_recent_gw_number: int = None
    teams_standing_info: List[TeamStandingInfo] = None

    def get_team_standing_info_by_name(
        self, team_name: str
    ) -> Optional[TeamStandingInfo]:
        for team_standing_info in self.teams_standing_info:
            if team_standing_info.team.team_name == team_name:
                return team_standing_info

        return None
