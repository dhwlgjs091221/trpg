import streamlit as st
from character_creator import character_creator_page
from board import game_board_page

st.set_page_config(page_title="TRPG App", layout="wide")

page = st.sidebar.selectbox("페이지 선택", ["캐릭터 생성", "게임 보드"])

if page == "캐릭터 생성":
    character_creator_page()
elif page == "게임 보드":
    game_board_page()