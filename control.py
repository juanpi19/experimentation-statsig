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

def rock_paper_scissors_control():
    st.title("Rock Paper Scissors Game")
    
    # Initialize session state for scores
    if 'player_score' not in st.session_state:
        st.session_state.player_score = 0
    if 'computer_score' not in st.session_state:
        st.session_state.computer_score = 0
    
    # Game choices
    choices = ["Rock", "Paper", "Scissors"]
    
    # Player selection
    player_choice = st.radio("Choose your move:", choices)
    
    # Play button
    if st.button("Play"):
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
    
    # Display current scores
    st.header("Scores")
    st.write(f"Player: {st.session_state.player_score}")
    st.write(f"Computer: {st.session_state.computer_score}")

