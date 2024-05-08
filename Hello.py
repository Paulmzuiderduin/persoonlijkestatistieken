import pandas as pd
import streamlit as st

# Initialize empty list in session_state to store actions
if "actions" not in st.session_state:
    st.session_state["actions"] = []

# Title and app description
st.title("Waterpolo Statistics Tracker")
st.write("Keep track of waterpolo actions during the match!")

# Define actions
actions = ["Balverlies", "Balverovering"]

# Create a sidebar for quarter selection
quarter_options = ["Periode 1", "Periode 2", "Periode", "Periode"]
selected_quarter = st.sidebar.selectbox("Selecteer periode", quarter_options)

# Create a 3-column layout for player selection
player_cols = st.columns(3)

# Player selection using radio buttons
player_options = {f"Player {i}": i for i in range(1, 15)}
selected_player = st.radio("Select Player", list(player_options.keys()), horizontal=True, key="player_select")

# Action selection using buttons
action_selection_col, _ = st.columns(2)  # Create columns for action selection and spacing
with action_selection_col:
    for action in actions:
        if st.button(action):
            # Add action to session_state list with selected player and quarter
            st.session_state["actions"].append({"Player": player_options[selected_player], "Action": action, "Quarter": selected_quarter})

# Reset button to clear actions
if st.button("Reset Actions"):
    st.session_state["actions"] = []  # Clear the actions list

# Display dataframe of actions
df = pd.DataFrame(st.session_state["actions"])
st.dataframe(df)

