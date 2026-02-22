import pandas as pd
from fantasy_cls import Standings, Team, TeamStandingsInfo
from typing import Optional


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


def get_head_to_head_table(matches: pd.DataFrame, league_entries: pd.DataFrame) -> pd.DataFrame:
    id_to_name = dict(zip(league_entries["id"], league_entries["entry_name"]))
    team_names = list(league_entries["entry_name"])

    # h2h[team_a][team_b] = [wins_of_a_vs_b, losses_of_a_vs_b]
    h2h = {name: {other: [0, 0] for other in team_names} for name in team_names}

    finished = matches[matches["finished"].astype(bool)]

    for _, match in finished.iterrows():
        t1 = id_to_name.get(match["league_entry_1"])
        t2 = id_to_name.get(match["league_entry_2"])
        if t1 is None or t2 is None:
            continue

        p1 = match["league_entry_1_points"]
        p2 = match["league_entry_2_points"]

        if p1 > p2:
            h2h[t1][t2][0] += 1
            h2h[t2][t1][1] += 1
        elif p2 > p1:
            h2h[t2][t1][0] += 1
            h2h[t1][t2][1] += 1
        # draws are not counted in W-L cells

    def get_stats(team):
        wins = sum(h2h[team][opp][0] for opp in team_names if opp != team)
        losses = sum(h2h[team][opp][1] for opp in team_names if opp != team)
        total = wins + losses
        pct = (wins / total * 100) if total > 0 else 0.0
        return wins, losses, pct

    stats = {team: get_stats(team) for team in team_names}
    sorted_teams = sorted(team_names, key=lambda t: stats[t][2], reverse=True)

    data = []
    for team in sorted_teams:
        row = {"Player": team}
        for opp in sorted_teams:
            if team == opp:
                row[opp] = None
            else:
                w, l = h2h[team][opp]
                row[opp] = f"{w}-{l}"
        wins, losses, pct = stats[team]
        row["Wins"] = wins
        row["Losses"] = losses
        row["%"] = f"{pct:.1f}%"
        data.append(row)

    return pd.DataFrame(data)


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
