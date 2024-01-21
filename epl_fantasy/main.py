import typer
from gameweeks import Gameweeks
from standings import initialize_standings, update_standings

app = typer.Typer()


@app.command()
def get_standings():
    standing = initialize_standings()

    for gameweek in Gameweeks.list():
        standing = update_standings(gameweek=gameweek, standings=standing)

    return standing
