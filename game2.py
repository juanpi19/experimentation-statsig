import streamlit as st
import random
from statsig import statsig
from statsig.statsig_event import StatsigEvent
from statsig.statsig_user import StatsigUser
import uuid 


secret_key = st.secrets["secret_key"]

def initialize_statsig(api_key: str):
    statsig.initialize(api_key)  # Initialize Statsig

def check_feature_gate(user, gate_name: str):
    return statsig.check_gate(StatsigUser(user), gate_name)

def render(user, gate_name: str):

    different_button_shape = check_feature_gate(user, gate_name)
    if different_button_shape:
        #st.success(f"Feature gate '{gate_name}' is ACTIVE for user '{user}'!")
        st.write('hello')
    else:
        #st.warning(f"Feature gate '{gate_name}' is INACTIVE for user '{user}'.")
        st.write('bye')

def main():
    user_id = str(uuid.uuid4())
    initialize_statsig(api_key=secret_key)
    render(user=user_id, gate_name='rock_paper_scissor_game')

if __name__ == '__main__':
    main()