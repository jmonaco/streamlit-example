import pandas as pd
import streamlit as st
from google.oauth2 import service_account
from gsheetsdb import connect

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["private_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

df = pd.DataFrame(rows[1:], columns=rows[0])

st.markdown('## st.dataframe')
st.dataframe(df)

st.markdown('## st.line_chart')
st.line_chart(df)

st.markdown('## st.area_chart')
st.area_chart(df)

st.markdown('## st.bar_chart')
st.bar_chart(df)

st.markdown('## st.altair_chart')
st.altair_chart(df)

st.markdown('## st.vega_lite_chart')
st.vega_lite_chart(df)

st.markdown('## st.plotly_chart')
st.plotly_chart(df)

st.markdown('## st.bokeh_chart')
st.bokeh_chart(df)

st.markdown('## st.pydeck_chart')
st.pydeck_chart(df)

st.markdown('## st.deck_gl_chart')
st.deck_gl_chart(df)

st.markdown('## st.graphviz_chart')
st.graphviz_chart(df)

st.markdown('## st.map')
st.map(df)