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

    # h2h[team_a][team_b] = [wins, draws, losses] of team_a vs team_b
    h2h = {name: {other: [0, 0, 0] for other in team_names} for name in team_names}

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
            h2h[t2][t1][2] += 1
        elif p2 > p1:
            h2h[t2][t1][0] += 1
            h2h[t1][t2][2] += 1
        else:
            h2h[t1][t2][1] += 1
            h2h[t2][t1][1] += 1

    def get_stats(team):
        wins = sum(h2h[team][opp][0] for opp in team_names if opp != team)
        draws = sum(h2h[team][opp][1] for opp in team_names if opp != team)
        losses = sum(h2h[team][opp][2] for opp in team_names if opp != team)
        total = wins + draws + losses
        pct = (wins / total * 100) if total > 0 else 0.0
        return wins, draws, losses, pct

    stats = {team: get_stats(team) for team in team_names}
    sorted_teams = sorted(team_names, key=lambda t: stats[t][3], reverse=True)

    data = []
    for team in sorted_teams:
        row = {"Player": team}
        for opp in sorted_teams:
            if team == opp:
                row[opp] = None
            else:
                w, d, l = h2h[team][opp]
                row[opp] = f"{w}-{d}-{l}"
        wins, draws, losses, pct = stats[team]
        row["W"] = wins
        row["D"] = draws
        row["L"] = losses
        row["%"] = f"{pct:.1f}%"
        data.append(row)

    return pd.DataFrame(data)


def get_recent_form(matches: pd.DataFrame, league_entries: pd.DataFrame, n: int = 5) -> dict:
    id_to_name = dict(zip(league_entries["id"], league_entries["entry_name"]))
    team_names = list(league_entries["entry_name"])

    finished = matches[matches["finished"].astype(bool)].sort_values("event")
    form = {team: [] for team in team_names}

    for _, match in finished.iterrows():
        t1 = id_to_name.get(match["league_entry_1"])
        t2 = id_to_name.get(match["league_entry_2"])
        if t1 is None or t2 is None:
            continue

        p1 = match["league_entry_1_points"]
        p2 = match["league_entry_2_points"]

        if p1 > p2:
            form[t1].append("W")
            form[t2].append("L")
        elif p2 > p1:
            form[t2].append("W")
            form[t1].append("L")
        else:
            form[t1].append("D")
            form[t2].append("D")

    return {team: results[-n:] for team, results in form.items()}


def get_rank_evolution(matches: pd.DataFrame, league_entries: pd.DataFrame) -> pd.DataFrame:
    id_to_name = dict(zip(league_entries["id"], league_entries["entry_name"]))
    team_names = list(league_entries["entry_name"])

    finished = matches[matches["finished"].astype(bool)].sort_values("event")
    all_gws = sorted(finished["event"].unique())

    # Accumulate league pts and fantasy pts per team per gameweek
    league_pts = {team: 0 for team in team_names}
    fantasy_pts = {team: 0 for team in team_names}

    data = []
    for gw in all_gws:
        gw_matches = finished[finished["event"] == gw]
        for _, match in gw_matches.iterrows():
            t1 = id_to_name.get(match["league_entry_1"])
            t2 = id_to_name.get(match["league_entry_2"])
            if t1 is None or t2 is None:
                continue

            p1 = match["league_entry_1_points"]
            p2 = match["league_entry_2_points"]
            fantasy_pts[t1] += p1
            fantasy_pts[t2] += p2

            if p1 > p2:
                league_pts[t1] += 3
            elif p2 > p1:
                league_pts[t2] += 3
            else:
                league_pts[t1] += 1
                league_pts[t2] += 1

        # Rank teams at this gameweek
        ranked = sorted(team_names, key=lambda t: (league_pts[t], fantasy_pts[t]), reverse=True)
        for rank, team in enumerate(ranked, start=1):
            data.append({"Team": team, "Gameweek": gw, "Rank": rank})

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
