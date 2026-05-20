import streamlit as st
import random

# Page Config
st.set_page_config(
    page_title="Rock Paper Scissors",
    page_icon="🎮",
    layout="centered"
)

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Title
st.markdown(
    "<h1 style='text-align:center; color:yellow;'>ROCK PAPER SCISSORS</h1>",
    unsafe_allow_html=True
)

st.write("## Choose One!")

# Function
def play(user_choice):
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "🤝 It's a Tie!"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "🎉 You Win!"

    else:
        result = "💻 Computer Wins!"

    return computer_choice, result


# Buttons
col1, col2, col3 = st.columns(3)

with col1:
    rock = st.button("🪨 Rock")

with col2:
    paper = st.button("📄 Paper")

with col3:
    scissors = st.button("✂️ Scissors")

# Game Logic
if rock:
    comp, result = play("Rock")

    st.success(f"""
    You: Rock  
    Computer: {comp}

    {result}
    """)

elif paper:
    comp, result = play("Paper")

    st.success(f"""
    You: Paper  
    Computer: {comp}

    {result}
    """)

elif scissors:
    comp, result = play("Scissors")

    st.success(f"""
    You: Scissors  
    Computer: {comp}

    {result}
    """)

