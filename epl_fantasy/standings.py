import pandas as pd
from fantasy_cls import Gameweek, Standings, TeamStandingsInfo
from teams import Teams


def get_standings_table(standings: Standings) -> pd.DataFrame:
    # Prepare a list to hold records
    data = []
    # Process the standing objects
    for rank, standing in enumerate(standings.teams_standings_info, start=1):
        record = {
            "Rank": rank,
            "Team Name": standing.team.team_name,
            "Manager": standing.team.manager_name,
            "W": standing.wins,
            "D": standing.draws,
            "L": standing.losses,
            "+": standing.points_scored,
            "Pts": standing.points,
        }
        data.append(record)
    # Convert the list of records to a DataFrame
    df = pd.DataFrame(data)
    return df


def initialize_standings() -> Standings:
    teams_standings_info = [
        TeamStandingsInfo(team=team) for team in Teams.list()
    ]
    return Standings(teams_standings_info=teams_standings_info)


def update_standings(gameweek: Gameweek, standings: Standings) -> Standings:
    standings.most_recent_gw_number = gameweek.number
    for fixture in gameweek.fixtures:
        home_team_points = fixture.home_team[1]
        away_team_points = fixture.away_team[1]
        if home_team_points is None or away_team_points is None:
            continue

        home_team_standings_info = standings.get_team_standings_info_by_name(
            fixture.home_team[0].team_name
        )
        away_team_standings_info = standings.get_team_standings_info_by_name(
            fixture.away_team[0].team_name
        )
        home_team_standings_info.points_scored += home_team_points
        away_team_standings_info.points_scored += away_team_points

        if home_team_points > away_team_points:
            home_team_standings_info.wins += 1
            home_team_standings_info.points += 3
            away_team_standings_info.losses += 1
        elif home_team_points < away_team_points:
            away_team_standings_info.wins += 1
            away_team_standings_info.points += 3
            home_team_standings_info.losses += 1
        else:
            away_team_standings_info.draws += 1
            away_team_standings_info.points += 1
            home_team_standings_info.draws += 1
            home_team_standings_info.points += 1

    standings.order_standing()
    return standings
