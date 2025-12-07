import typer
from api_draft import get_league_standings
from standings import Standings, build_standings_from_api_data

app = typer.Typer()


@app.command()
def get_standings() -> Standings:
    standings_df, last_gameweek_processed = get_league_standings()
    return build_standings_from_api_data(
        standings_df=standings_df, last_gameweek_processed=last_gameweek_processed
    )
