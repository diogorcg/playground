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
    manager_name: str
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
class TeamStandingsInfo:
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
class Standings:
    most_recent_gw_number: int = None
    teams_standings_info: List[TeamStandingsInfo] = None

    def __post_init__(self):
        if self.teams_standings_info is None or (
            len(self.teams_standings_info) == 0
        ):
            return
        self.order_standing()

    def get_team_standings_info_by_name(
        self, team_name: str
    ) -> Optional[TeamStandingsInfo]:
        for team_standings_info in self.teams_standings_info:
            if team_standings_info.team.team_name == team_name:
                return team_standings_info

        return None

    def order_standing(self):
        self.teams_standings_info = sorted(
            self.teams_standings_info,
            key=lambda team_standings_info: (
                team_standings_info.points,
                team_standings_info.points_scored,
            ),
            reverse=True,
        )
