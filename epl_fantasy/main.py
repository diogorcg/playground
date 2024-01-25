import pandas as pd
import typer
from api_draft import get_league_standings
from standings import Standings, initialize_standings

app = typer.Typer()


@app.command()
def get_standings():
    standing = initialize_standings()

    second_part_standings, last_gamweek_processed = get_league_standings()
    standing.most_recent_gw_number = last_gamweek_processed
    standing = update_standings(standing, second_part_standings)

    standing.order_standing()

    return standing


def update_standings(standing: Standings, second_part_df: pd.DataFrame):
    for team_standing_info in standing.teams_standings_info:
        team_second_part = second_part_df[
            second_part_df["manager_name"]
            == team_standing_info.team.manager_name
        ].iloc[0]
        team_standing_info.team.second_team_name = team_second_part[
            "entry_name"
        ]
        team_standing_info.matches_won += team_second_part["matches_won"]
        team_standing_info.matches_lost += team_second_part["matches_lost"]
        team_standing_info.matches_drawn += team_second_part["matches_drawn"]
        team_standing_info.total += team_second_part["total"]
        team_standing_info.points_against += team_second_part["points_against"]
        team_standing_info.points_for += team_second_part["points_for"]

    return standing
