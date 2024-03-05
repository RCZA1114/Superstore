import streamlit as st
from datetime import timedelta
import plotly.express as px
from data import *

st.set_page_config(
    page_title="Dashboard",
    page_icon="👋",
)


st.title("Dashboard")




data = superstore()
select_area = st.selectbox('Select Area', ('Supplies', 'Countries'))

if select_area == 'Countries':
    select_measure = st.selectbox('Select Measure', ('Sales', 'Profit'))

    select_region = data["Region"].unique()
    selected_region = st.selectbox('Select Region', select_region)

    df = data[data["Region"] == selected_region]

    groupcountry = df.groupby('Country').sum()[select_measure]
    chart = px.bar(groupcountry)


    st.plotly_chart(chart, use_container_width=True)


    #_____________________________________________________________
    select_country = df['Country'].unique()
    selected_country = st.selectbox('Select Country', select_country)

    dfr = df[df["Country"] == selected_country]

    groupregion = dfr.groupby('State').sum()[select_measure]
    chartregion = px.bar(groupregion)
    st.plotly_chart(chartregion, use_container_width=True)

    #______________________________________________________________
    select_state = dfr['State'].unique()
    selected_state = st.selectbox('Select State', select_state)

    dfs = dfr[dfr["State"] == selected_state]

    groupcity = dfs.groupby('City').sum()[select_measure]
    chartcity = px.bar(groupcity)
    st.plotly_chart(chartcity, use_container_width=True)

else:
    select_measure = st.selectbox('Select Measure', ('Sales', 'Profit'))

    select_segment = data["Segment"].unique()
    selected_segment = st.selectbox('Select Segment', select_segment)

    df = data[data["Segment"] == selected_segment]

    groupseg = df.groupby('Category').sum()[select_measure]
    chart = px.bar(groupseg)

    st.plotly_chart(chart, use_container_width=True)
    
    #___________________________________________________________________
    select_cat = data["Category"].unique()
    selected_cat = st.selectbox('Select Category', select_cat)

    dfc = df[df["Category"] == selected_cat]

    groupcat = dfc.groupby('Sub-Category').sum()[select_measure]
    chartc = px.bar(groupcat)

    st.plotly_chart(chartc, use_container_width=True)