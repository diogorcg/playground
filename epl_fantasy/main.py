import typer
from gameweeks import Gameweeks

from epl_fantasy.standings import initialize_standings, update_standings

app = typer.Typer()


@app.command()
def get_standings():
    standing = initialize_standings()

    for gameweek in Gameweeks.list():
        standing = update_standings(gameweek=gameweek, standings=standing)

    return standing


if __name__ == "__main__":
    gg = get_standings()
    print(1)
