import streamlit as st
from main import get_standings
from standings import get_standings_table

standings = get_standings()

standings_df = get_standings_table(standings)


st.set_page_config(page_title="EPL Fantasy Mamar é vida")

st.title("Mamar é vida Standings")

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
