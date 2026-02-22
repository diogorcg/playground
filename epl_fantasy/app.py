import altair as alt
import pandas as pd
import streamlit as st
from api_draft import get_matches_and_entries
from main import get_standings
from standings import get_head_to_head_table, get_rank_evolution, get_recent_form, get_standings_table

standings = get_standings()
standings_df = get_standings_table(standings)

matches, league_entries = get_matches_and_entries()
h2h_df = get_head_to_head_table(matches, league_entries)
recent_form = get_recent_form(matches, league_entries)
rank_evolution_df = get_rank_evolution(matches, league_entries)


st.set_page_config(page_title="EPL Fantasy Mamar é vida", layout="wide")

st.markdown("<h1 style='text-align: center;'>Mamar é vida</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Standings</h3>", unsafe_allow_html=True)

ROW_COLORS = {
    1: "#FFD700",   # gold - Camisola de vencedor
    2: "#d4edda",   # light green - Mamam à pala
    3: "#d4edda",
    4: "#d4edda",
    5: "#f8d7da",   # light red - Pagam a francesa
    6: "#f8d7da",
    7: "#f8d7da",
    8: "#f8d7da",
}

table_css = """
<style>
table {
    margin: 0 auto;
}
.table td, .table th {
    text-align: center;
    word-break: normal;
    overflow-wrap: normal;
    padding: 4px 10px;
}
</style>
"""

FORM_COLORS = {"W": "#28a745", "D": "#e0a800", "L": "#dc3545"}

def form_badges(results):
    badges = ""
    for r in results:
        color = FORM_COLORS.get(r, "#6c757d")
        badges += f'<span style="background:{color};color:white;border-radius:3px;padding:1px 5px;margin:1px;font-size:11px;font-weight:bold;">{r}</span>'
    return badges

header_cells = "".join(f"<th>{col}</th>" for col in standings_df.columns) + "<th>Forma</th>"
standings_rows = ""
for rank, (_, row) in enumerate(standings_df.iterrows(), start=1):
    color = ROW_COLORS.get(rank, "")
    style = f' style="background-color: {color};"' if color else ""
    standings_rows += f"<tr{style}>"
    for val in row:
        standings_rows += f"<td>{val}</td>"
    form = recent_form.get(row["Team Name"], [])
    standings_rows += f"<td>{form_badges(form)}</td>"
    standings_rows += "</tr>"

standings_html = f"""
<table class="table table-hover">
  <thead><tr>{header_cells}</tr></thead>
  <tbody>{standings_rows}</tbody>
</table>
<div style="margin: 10px auto; width: fit-content; font-size: 13px;">
  <span style="display:inline-block; width:14px; height:14px; background:#FFD700; margin-right:4px; vertical-align:middle;"></span>Camisola e mama à pala &nbsp;&nbsp;
  <span style="display:inline-block; width:14px; height:14px; background:#d4edda; margin-right:4px; vertical-align:middle;"></span>Mamam à pala &nbsp;&nbsp;
  <span style="display:inline-block; width:14px; height:14px; background:#f8d7da; margin-right:4px; vertical-align:middle;"></span>Pagam a francesa
</div>
"""

st.markdown(table_css + standings_html, unsafe_allow_html=True)

# Head to Head table
st.markdown("<h3 style='text-align: center;'>Head to Head</h3>", unsafe_allow_html=True)

team_cols = [c for c in h2h_df.columns if c not in ["Player", "W", "D", "L", "%"]]

h2h_html_rows = ""
for _, row in h2h_df.iterrows():
    h2h_html_rows += "<tr>"
    for col in h2h_df.columns:
        val = row[col]
        if col in team_cols and (val is None or (isinstance(val, float) and pd.isna(val))):
            h2h_html_rows += '<td style="background-color: black;"></td>'
        else:
            h2h_html_rows += f"<td>{val}</td>"
    h2h_html_rows += "</tr>"

header_cells = "".join(f"<th>{col}</th>" for col in h2h_df.columns)
h2h_html = f"""
<table class="table table-striped table-hover">
  <thead><tr>{header_cells}</tr></thead>
  <tbody>{h2h_html_rows}</tbody>
</table>
"""

st.markdown(table_css + h2h_html, unsafe_allow_html=True)

# Rank evolution chart
st.markdown("<h3 style='text-align: center;'>Standings Evolution</h3>", unsafe_allow_html=True)

n_teams = rank_evolution_df["Rank"].max()
n_gameweeks = rank_evolution_df["Gameweek"].nunique()
chart_width = max(900, n_gameweeks * 55)

chart = (
    alt.Chart(rank_evolution_df)
    .mark_line(point=True)
    .encode(
        x=alt.X("Gameweek:O", title="Gameweek"),
        y=alt.Y("Rank:Q", title="Position", scale=alt.Scale(domain=[n_teams, 1], nice=False), axis=alt.Axis(tickMinStep=1)),
        color=alt.Color("Team:N", title="Team"),
        tooltip=["Team", "Gameweek", "Rank"],
    )
    .properties(width=chart_width, height=400)
)

st.altair_chart(chart)
