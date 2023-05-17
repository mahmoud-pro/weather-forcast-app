import streamlit as st
import plotly.express as px
from backend import get_data

st.set_page_config(page_title="Weather Forcast", page_icon="assets/images/favicon.ico",
                   layout="centered", initial_sidebar_state="auto", menu_items=None)

st.title("Weather Forcast For Next Days")
place = st.text_input("Place:")

forcast_days = st.slider("Forcast Days:", 1, 5, help="select number for forcast days")

choice = st.selectbox("Select Data To View", ["Temperature", "Sky"])

st.subheader(f"{choice} for {forcast_days} next days in {place}")

# data = get_data(place, forcast_days)

if place:
    filter_data = get_data(place, forcast_days)

    if choice == "Temperature":
        temperatures = [dt["main"]["temp"] for dt in filter_data]
        dates = [d['dt_txt'] for d in filter_data]

        figure = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if choice == "Sky":
        images = {
                  "Clear": "assets/images/clear.png",
                  "Clouds": "assets/images/cloud.png",
                  "Rain": "assets/images/rain.png",
                  "Snow": "assets/images/snow.png",
                  }
        sky_conditions = [dt["weather"][0]["main"] for dt in filter_data]

        image_path = [images[con] for con in sky_conditions]
        print(sky_conditions)
        st.image(image_path, width=115)
