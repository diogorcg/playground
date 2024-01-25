import streamlit as st
from main import get_standings
from standings import get_standings_table

standings = get_standings()

latest_processed_gameweek = min(21, standings.most_recent_gw_number)
standings_df = get_standings_table(standings)


st.set_page_config(page_title="EPL Fantasy Here-we-go")

st.title("Here we go Standings")

st.markdown(f"Latest gameweek processed: **{latest_processed_gameweek}**")


# Center the table elements using HTML & CSS
df_html = standings_df.to_html(
    classes="table table-striped table-hover", index=False
)


centered_df_html_css = """
<style>
table {
    margin-left: auto;
    margin-right: auto;
    width: 100%;
}
.table td, .table th {
    text-align: center;
}
</style>
"""

centered_df_html = centered_df_html_css + df_html

# Write the HTML string to the Streamlit app
st.markdown(centered_df_html, unsafe_allow_html=True)
