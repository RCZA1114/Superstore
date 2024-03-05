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

select_segment = data['RegionS'].unique()
    
selected_segment = st.selectbox('Select Segment', select_segment)

df = data[data['Segment'] == selected_segment]

groupseg = df.groupby('Category').sum()[select_measure]
chart = px.bar(groupseg)

st.plotly_chart(chart, use_container_width=True)
    
    #___________________________________________________________________
select_cat = data['Category'].unique()
selected_cat = st.selectbox('Select Category', select_cat)

dfc = df[df['Category'] == selected_cat]

groupcat = dfc.groupby('Sub-Category').sum()[select_measure]
chartc = px.bar(groupcat)

st.plotly_chart(chartc, use_container_width=True)
