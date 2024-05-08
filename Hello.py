import pandas as pd
import streamlit as st

# Initialize empty list in session_state to store actions
if "acties" not in st.session_state:
    st.session_state["acties"] = []

# Title and app description
st.title("Waterpolo Statistieken Tracker")
st.write("Hou bij welke waterpolo acties er tijdens de wedstrijd plaatsvinden!")

# Define action groups and their corresponding actions (translated)
action_groups = {
    "Schoten": ["Doelpunt", "Geen Doelpunt"],
    "Passes": ["Goede Pass", "Slechte Pass"],
}

# Create a sidebar for quarter selection (translated)
quarter_options = ["Periode 1", "Periode 2", "Periode 3", "Periode 4"]
selected_quarter = st.sidebar.selectbox("Selecteer periode", quarter_options)

# Create a larger layout for player selection (translated)
player_cols = st.columns(3)  # Use 3 columns for players

# Player selection using radio buttons (translated)
player_options = {f"Speler {i}": i for i in range(1, 15)}
selected_player = st.radio("Selecteer Speler", list(player_options.keys()), horizontal=True, key="player_select")


def create_action_selection(group_name, actions):
    action_col1, action_col2 = st.columns(2)  # Two columns for actions
    with action_col1:
        st.subheader(group_name)
        for action in actions:
            if st.button(action):
                # Add action to session_state list with selected player, quarter, and group
                st.session_state["acties"].append(
                    {
                        "Speler": player_options[selected_player],
                        "Actie": action,
                        "Periode": selected_quarter,
                    }
                )


# Action selection using buttons for each action, displayed horizontally
action_selection_col1, action_selection_col2 = st.columns(2)  # Two columns for action groups
with action_selection_col1:
    create_action_selection("Schoten", action_groups["Schoten"])
with action_selection_col2:
    create_action_selection("Passes", action_groups["Passes"])

# Reset button and "Delete Last Action" button (translated)
reset_col1, delete_col1 = st.columns(2)
with reset_col1:
    if st.button("Reset Acties"):
        st.session_state["acties"] = []  # Clear the actions list
with delete_col1:
    if st.button("Verwijder Laatste Actie"):
        if st.session_state["acties"]:  # Check if there are any actions
            st.session_state["acties"].pop()  # Remove the last action from the list

# Display dataframe of actions (translated)
df = pd.DataFrame(st.session_state["acties"])

# Select only 'Speler' and 'Actie' columns (excluding 'Groep')
df_to_display = df[['Speler', 'Actie', 'Periode']]  # Select 'Periode' and 'Actie'

st.dataframe(df_to_display)

# Comment out the pass counting section

# # Calculate pass counts per player
# # ... (previous pass counting logic)

# Display dataframe with pass counts (commented out)
# st.subheader("Passen per Speler")
# st.dataframe(pass_counts)
