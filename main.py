#!/usr/bin/env python3
import streamlit as st
from hide_watermark import hide_watermark

st.set_page_config(layout="wide")
st.title("Gin Scorecard")
st.text("We will be using this app to keep score")


def get_player_names():
    with st.container():
        COLUMN_1, COLUMN_2 = st.columns(2)

        with COLUMN_1:
            P1_NAME = st.text_input("Player one's name:")

        with COLUMN_2:
            P2_NAME = st.text_input("Player two's name:")

        if P1_NAME and P2_NAME:
            st.success(f"Welcome {P1_NAME} and {P2_NAME}!")
            st.snow()

    return P1_NAME, P2_NAME


if __name__ == "__main__":
    P1_NAME, P2_NAME = get_player_names()
    hide_watermark()
