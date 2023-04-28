import streamlit as st
import pandas as pd


st.set_page_config(page_title="Weather Forcast", page_icon="assets/images/favicon.ico",
                   layout="centered", initial_sidebar_state="auto", menu_items=None)

st.title("Weather Forcast For Next Days")
place = st.text_input("Place:")

forcast_days = st.slider("Forcast Days:", 1, 5, help="select number for forcast days")

choice = st.selectbox("Select Data To View", ["Temperature", "Sky"])

st.subheader(f"{choice} for {forcast_days} next days in {place}")
