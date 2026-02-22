import pandas as pd
import streamlit as st
from api_draft import get_matches_and_entries
from main import get_standings
from standings import get_head_to_head_table, get_standings_table

standings = get_standings()
standings_df = get_standings_table(standings)

matches, league_entries = get_matches_and_entries()
h2h_df = get_head_to_head_table(matches, league_entries)


st.set_page_config(page_title="EPL Fantasy Mamar é vida", layout="wide")

st.markdown("<h1 style='text-align: center;'>Mamar é vida</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Standings</h3>", unsafe_allow_html=True)

# Center the table elements using HTML & CSS
df_html = standings_df.to_html(
    classes="table table-striped table-hover", index=False
)


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

centered_df_html = table_css + df_html

# Write the HTML string to the Streamlit app
st.markdown(centered_df_html, unsafe_allow_html=True)

# Head to Head table
st.markdown("<h3 style='text-align: center;'>Head to Head</h3>", unsafe_allow_html=True)

team_cols = [c for c in h2h_df.columns if c not in ["Player", "Wins", "Losses", "%"]]

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
