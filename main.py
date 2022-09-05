#!/usr/bin/env python3
import streamlit as st
import time
from hide_watermark import hide_watermark

st.set_page_config(
    layout="wide",
    page_title="Gin Scorecard",
)
st.title("Gin Scorecard")
st.text("We use this app to keep score in Gin")


def get_player_names():
    placeholder = st.empty()
    with placeholder.container():
        PLAYER1, PLAYER2 = st.columns(2)

        P1_NAME = PLAYER1.text_input("Player one's name:")
        P2_NAME = PLAYER2.text_input("Player two's name:")

        if P1_NAME and P2_NAME:
            st.success(f"Welcome {P1_NAME} and {P2_NAME}!")

    return P1_NAME, P2_NAME, placeholder


def add_score(OLD_SCORE, CHANGE):
    return OLD_SCORE + CHANGE


def subtract_score(OLD_SCORE, CHANGE):
    return OLD_SCORE - CHANGE


if __name__ == "__main__":
    st.session_state["NEW_GAME"] = "True"

    if st.session_state["NEW_GAME"] == "True":
        P1_NAME, P2_NAME, placeholder = get_player_names()
        st.session_state["P1_NAME"] = P1_NAME
        st.session_state["P2_NAME"] = P2_NAME
        st.session_state["P1_SCORE"] = 0
        st.session_state["P2_SCORE"] = 0
        st.session_state["NEW_GAME"] = "False"

    if st.session_state["NEW_GAME"] == "False":
        if P1_NAME and P2_NAME:
            time.sleep(2)
            placeholder.empty()

    PLAYER1, PLAYER2 = st.columns(2)
    if P1_NAME and P2_NAME:
        PLAYER1.subheader(st.session_state["P1_NAME"])
        PLAYER2.subheader(st.session_state["P2_NAME"])

    (
        PLAYER1_SCORE_COUNT,
        PLAYER1_CHANGE,
        PLAYER2_SCORE_COUNT,
        PLAYER2_CHANGE,
    ) = st.columns(4)

    PLAYER1_SCORE_COUNT.metric(label="Score", value=st.session_state["P1_SCORE"])
    PLAYER2_SCORE_COUNT.metric(label="Score", value=st.session_state["P2_SCORE"])

    hide_watermark()
