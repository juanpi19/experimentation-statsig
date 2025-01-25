import streamlit as st
import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Draw"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "Player"
    else:
        return "Computer"


def rock_paper_scissors_treatment():

    # Initialize session state for scores if not already set
    if 'player_score' not in st.session_state:
        st.session_state.player_score = 0
    if 'computer_score' not in st.session_state:
        st.session_state.computer_score = 0

    # Game choices
    choices = ["Rock", "Paper", "Scissors"]

    # Title and current scores
    st.title("Rock Paper Scissors")
    st.write(f"Player Score: {st.session_state.player_score}")
    st.write(f"Computer Score: {st.session_state.computer_score}")

    # Create columns for buttons
    col1, col2, col3 = st.columns(3)

    # Player selection buttons
    with col1:
        rock_button = st.button("Rock")
    with col2:
        paper_button = st.button("Paper")
    with col3:
        scissors_button = st.button("Scissors")

    # Determine which button was pressed
    player_choice = None
    if rock_button:
        player_choice = "Rock"
    elif paper_button:
        player_choice = "Paper"
    elif scissors_button:
        player_choice = "Scissors"

    # Game logic
    if player_choice:
        # Computer's random choice
        computer_choice = random.choice(choices)
        
        # Display choices
        st.write(f"Your choice: {player_choice}")
        st.write(f"Computer's choice: {computer_choice}")
        
        # Determine winner
        result = determine_winner(player_choice, computer_choice)
        
        # Update scores
        if result == "Player":
            st.session_state.player_score += 1
            st.success("You won this round!")
        elif result == "Computer":
            st.session_state.computer_score += 1
            st.error("Computer won this round!")
        else:
            st.warning("It's a draw!")