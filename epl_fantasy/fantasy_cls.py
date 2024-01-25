from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class FirstRoundInfo:
    matches_won: int
    matches_drawn: int
    matches_lost: int
    points_for: int
    points_against: int
    total: int


@dataclass
class Team:
    manager_name: str
    team_name: str
    first_round_info: FirstRoundInfo
    second_team_name: str = None


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
    matches_won: int = None
    matches_drawn: int = None
    matches_lost: int = None
    total: int = None
    points_for: int = None
    points_against: int = None

    def __post_init__(self):
        self.matches_won = self.team.first_round_info.matches_won
        self.matches_drawn = self.team.first_round_info.matches_drawn
        self.matches_lost = self.team.first_round_info.matches_lost
        self.points_for = self.team.first_round_info.points_for
        self.total = self.team.first_round_info.total
        self.points_against = self.team.first_round_info.points_against


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
                team_standings_info.total,
                team_standings_info.points_for,
            ),
            reverse=True,
        )
