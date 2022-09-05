#!/usr/bin/env python3
import streamlit as st
import time
from hide_watermark import hide_watermark

st.set_page_config(layout="wide")
st.title("Gin Scorecard")
st.text("We use this app to keep score in Gin")


def get_player_names():
    placeholder = st.empty()
    with placeholder.container():
        COLUMN_1, COLUMN_2 = st.columns(2)

        with COLUMN_1:
            P1_NAME = st.text_input("Player one's name:")

        with COLUMN_2:
            P2_NAME = st.text_input("Player two's name:")

        if P1_NAME and P2_NAME:
            st.success(f"Welcome {P1_NAME} and {P2_NAME}!")

    return P1_NAME, P2_NAME, placeholder


if __name__ == "__main__":
    P1_NAME, P2_NAME, placeholder = get_player_names()
    if P1_NAME and P2_NAME:
        time.sleep(3)
        placeholder.empty()
        COLUMN_1, COLUMN_2 = st.columns(2)
        with COLUMN_1:
            st.subheader(f"{P1_NAME}")
            st.metric(label="Score", value="0", delta="0")
        with COLUMN_2:
            st.subheader(f"{P2_NAME}")
            st.metric(label="Score", value="0", delta="0")
    hide_watermark()