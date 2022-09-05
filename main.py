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
    st.write("Starting new session")
    st.session_state["ROUND_COMPLETE"] = "False"
    if "NEW_GAME" not in st.session_state:
        P1_NAME, P2_NAME, placeholder = get_player_names()
        if P1_NAME and P2_NAME:
            st.session_state["P1_NAME"] = P1_NAME
            st.session_state["P2_NAME"] = P2_NAME
            st.session_state["P1_SCORE"] = 0
            st.session_state["P2_SCORE"] = 0
            st.session_state["NEW_GAME"] = "False"
            time.sleep(1)
            placeholder.empty()

    PLAYER1, SPACER1, CHANGE, SPACER2, PLAYER2 = st.columns(5)
    if "P1_NAME" in st.session_state and "P2_NAME" in st.session_state:
        PLAYER1.subheader(st.session_state["P1_NAME"])
        PLAYER2.subheader(st.session_state["P2_NAME"])
        SCORE1 = PLAYER1.metric(label="Score", value=st.session_state["P1_SCORE"])
        SCORE2 = PLAYER2.metric(label="Score", value=st.session_state["P2_SCORE"])
        WINNER = CHANGE.radio(
            "Round Winner:",
            (
                f'{st.session_state["P1_NAME"]}',
                f'{st.session_state["P2_NAME"]}',
                "Draw",
            ),
            key="winner",
        )
        POINT_CHANGE = CHANGE.number_input(label="Point Change", value=0)
        ADJUST_SCORE = CHANGE.button(label="Adjust Score")
        RESET_SCORE = CHANGE.button(label="Reset Score")
        if ADJUST_SCORE:
            if WINNER == f'{st.session_state["P1_NAME"]}':
                st.session_state["P1_SCORE"] += POINT_CHANGE
                SCORE1.value = st.session_state["P1_SCORE"]
            elif WINNER == f'{st.session_state["P2_NAME"]}':
                st.session_state["P2_SCORE"] += POINT_CHANGE
                SCORE2.value = st.session_state["P2_SCORE"]
            else:
                pass
            # Reruning script to update score on score adjustment
            st.experimental_rerun()

        # SET SCORES BACK TO ZERO IF RESET SCORE BUTTON IS CLICKED
        if RESET_SCORE:
            st.session_state["P1_SCORE"] = 0
            st.session_state["P2_SCORE"] = 0
            SCORE1.value = st.session_state["P1_SCORE"]
            SCORE2.value = st.session_state["P2_SCORE"]
            st.experimental_rerun()

        # CREATE CELEBRATORY BALLOONS ON CROSSING 100 POINTS
        if st.session_state["P1_SCORE"] >= 100:
            SCORE1.value = st.session_state["P1_SCORE"]
            st.title(f"CONGRATULATIONS {st.session_state['P1_NAME']}")
            st.balloons()
        if st.session_state["P2_SCORE"] >= 100:
            SCORE2.value = st.session_state["P2_SCORE"]
            st.title(f"CONGRATULATIONS {st.session_state['P2_NAME']}")
            st.balloons()

    hide_watermark()
