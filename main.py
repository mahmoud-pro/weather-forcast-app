import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Weather Forcast", page_icon="assets/images/favicon.ico",
                   layout="centered", initial_sidebar_state="auto", menu_items=None)

st.title("Weather Forcast For Next Days")
place = st.text_input("Place:")

forcast_days = st.slider("Forcast Days:", 1, 5, help="select number for forcast days")

choice = st.selectbox("Select Data To View", ["Temperature", "Sky"])

st.subheader(f"{choice} for {forcast_days} next days in {place}")


def get_data(days):
    dates = ["2022-02-02", "2023-02-02", "2024-02-02"]
    temperature = [10, 15, 30]
    temperature = [days * i for i in temperature]

    return dates, temperature


d, t = get_data(forcast_days)

figure = px.line(x=d, y=t, labels={"x": "Dates", "y": "Temperature (C)"})
st.plotly_chart(figure)

