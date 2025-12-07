import pandas as pd
from fantasy_cls import Standings, Team, TeamStandingsInfo


def get_standings_table(standings: Standings) -> pd.DataFrame:
    # Prepare a list to hold records
    data = []
    # Process the standing objects
    for rank, standing in enumerate(standings.teams_standings_info, start=1):
        record = {
            "Rank": rank,
            "Team Name": standing.team.team_name,
            "Manager": standing.team.manager_name,
            "W": standing.matches_won,
            "D": standing.matches_drawn,
            "L": standing.matches_lost,
            "+": standing.points_for,
            "-": standing.points_against,
            "Pts": standing.total,
        }
        data.append(record)
    # Convert the list of records to a DataFrame
    df = pd.DataFrame(data)
    return df


def build_standings_from_api_data(
    standings_df: pd.DataFrame, last_gameweek_processed: int
) -> Standings:
    """Create standings using the Draft API payload only."""

    def _safe_int(value) -> int:
        if pd.isna(value):
            return 0
        return int(value)

    teams_standings_info = []
    for _, row in standings_df.iterrows():
        team = Team(
            manager_name=row.get("manager_name", ""),
            team_name=row.get("entry_name", ""),
        )
        teams_standings_info.append(
            TeamStandingsInfo(
                team=team,
                matches_won=_safe_int(row.get("matches_won")),
                matches_drawn=_safe_int(row.get("matches_drawn")),
                matches_lost=_safe_int(row.get("matches_lost")),
                total=_safe_int(row.get("total")),
                points_for=_safe_int(row.get("points_for")),
                points_against=_safe_int(row.get("points_against")),
            )
        )

    return Standings(
        most_recent_gw_number=last_gameweek_processed,
        teams_standings_info=teams_standings_info,
    )
