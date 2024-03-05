import streamlit as st
from datetime import timedelta
import plotly.express as px
from data import *

data = pd.read_csv("superstore.csv")

select_measure = st.selectbox('Select Measure', ('Sales', 'Profit'))
groupreg = data.groupby('Region').sum()[select_measure]
plot = px.bar(groupreg, title=f"{select_measure} chart of all regions.")
gac = data.groupby('Country').sum()[select_measure]
plot2 = px.bar(gac, title=f"{select_measure} chart of all countries.")
st.plotly_chart(plot, use_container_width=True)
st.plotly_chart(plot2, use_container_width=True)
#_________________________________________________________________________________

select_region = data["Region"].unique()
selected_region = st.selectbox('Select Region', select_region)

df = data[data["Region"] == selected_region]

groupcountry = df.groupby('Country').sum()[select_measure]
chart = px.bar(groupcountry, title=f"{select_measure} chart of each country from {selected_region}.")


st.plotly_chart(chart, use_container_width=True)


    #_____________________________________________________________
select_country = df['Country'].unique()
selected_country = st.selectbox('Select Country', select_country)

dfr = df[df["Country"] == selected_country]

groupregion = dfr.groupby('State').sum()[select_measure]
chartregion = px.bar(groupregion, title=f"{select_measure} chart of each state from {selected_country}.")
st.plotly_chart(chartregion, use_container_width=True)

    #______________________________________________________________
select_state = dfr['State'].unique()
selected_state = st.selectbox('Select State', select_state)

dfs = dfr[dfr["State"] == selected_state]

groupcity = dfs.groupby('City').sum()[select_measure]
chartcity = px.bar(groupcity, title=f"{select_measure} chart of each city from {selected_state}.")
st.plotly_chart(chartcity, use_container_width=True)

