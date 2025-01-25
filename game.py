import streamlit as st
import random
from control import rock_paper_scissors_control
from treatment import rock_paper_scissors_treatment
from statsig import statsig
from statsig.statsig_event import StatsigEvent
from statsig.statsig_user import StatsigUser
import uuid 

secret_key = st.secrets["secret_key"]

def initialize_statsig(api_key: str):
    statsig.initialize(api_key)  

def check_feature_gate(user, gate_name: str):
    return statsig.check_gate(StatsigUser(user), gate_name)

def render(user, gate_name: str):
    statsig.log_event(StatsigEvent(StatsigUser(user), 'game_played'))
    different_button_shape = check_feature_gate(user, gate_name)

    if different_button_shape:
        rock_paper_scissors_treatment()

    else:
        rock_paper_scissors_control()

if "user_id" not in st.session_state:
    st.session_state["user_id"] = str(uuid.uuid4())

def main():
    user_id = st.session_state["user_id"] #user_id = str(uuid.uuid4())
    print(user_id)
    initialize_statsig(api_key=secret_key)
    render(user=user_id, gate_name='change_button_shape')

if __name__ == '__main__':
    main()

