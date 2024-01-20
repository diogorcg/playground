import typer
from fantasy_cls import Gameweek, Standing, TeamStandingInfo
from gameweeks import Gameweeks
from teams import Teams

app = typer.Typer()


@app.command()
def get_standing():
    standing = initialize_standing()

    for gameweek in Gameweeks.list():
        standing = process_gameweek(gameweek=gameweek, standing=standing)

    return standing


def initialize_standing() -> Standing:
    teams_standing_info = [
        TeamStandingInfo(team=team) for team in Teams.list()
    ]
    return Standing(teams_standing_info=teams_standing_info)


def process_gameweek(gameweek: Gameweek, standing: Standing) -> Standing:
    standing.most_recent_gw_number = gameweek.number
    for fixture in gameweek.fixtures:
        home_team_points = fixture.home_team[1]
        away_team_points = fixture.away_team[1]
        if home_team_points is None or away_team_points is None:
            continue

        home_team_standing_info = standing.get_team_standing_info_by_name(
            fixture.home_team[0].team_name
        )
        away_team_standing_info = standing.get_team_standing_info_by_name(
            fixture.away_team[0].team_name
        )
        home_team_standing_info.points_scored += home_team_points
        away_team_standing_info.points_scored += away_team_points

        if home_team_points > away_team_points:
            home_team_standing_info.wins += 1
            home_team_standing_info.points += 3
            away_team_standing_info.losses += 1
        elif home_team_points < away_team_points:
            away_team_standing_info.wins += 1
            away_team_standing_info.points += 3
            home_team_standing_info.losses += 1
        else:
            away_team_standing_info.draws += 1
            away_team_standing_info.points += 1
            home_team_standing_info.draws += 1
            home_team_standing_info.points += 1

    return standing
