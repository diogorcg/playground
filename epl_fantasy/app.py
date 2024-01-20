import streamlit as st
from main import get_standing
st.set_page_config(page_title="EPL Fantasy Here-we-go")

st.title("Standings Here we go")

standing = get_standing()

latest_processed_gameweek = standing.most_recent_gw_number

st.markdown(f"### Latest gameweek processed: {latest_processed_gameweek}")
