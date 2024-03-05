import streamlit as st
from datetime import timedelta
import plotly.express as px
from data import *

st.set_page_config(
    page_title="Dashboard",
    page_icon="👋",
)


st.title("Dashboard")

@st.cache_data
def load_data():
    data = pd.read_csv('superstore.csv')



data = load_data()
select_measure = st.selectbox('Select Measure', ('Sales', 'Profit'))


