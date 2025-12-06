import pandas as pd
import requests


def get_league_standings():
    league_info = requests.get(
        "https://draft.premierleague.com/api/league/623523/details"
    ).json()

    standings = pd.DataFrame(league_info["standings"])
    league_entries = pd.DataFrame(league_info["league_entries"])
    league_entries["manager_name"] = (
        league_entries["player_first_name"]
        + " "
        + league_entries["player_last_name"]
    )

    matches = pd.DataFrame(league_info["matches"])
    last_gamweek_processed = matches.sort_values(
        by=["finished", "event"], ascending=[False, True]
    ).iloc[0]["event"]

    standings = pd.merge(
        standings,
        league_entries,
        left_on="league_entry",
        right_on="id",
        how="inner",
    )

    return standings, last_gamweek_processed
