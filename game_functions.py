# Example function structure for `game_functions.py`
def handle_action(action, session):
    # Initialize game if not already done
    if 'current_room' not in session:
        start_new_game(session)
    
    # Sample action handlers
    if action.startswith('go to'):
        return move_rooms(action, session)
    elif action.startswith('take'):
        return take_item(action, session)
    elif action == 'talk to gardener':
        return talk_to_gardener(session)
    
    # More complex interactions...
    return "You're not sure what to do."

def start_new_game(session):
    session['current_room'] = 'entrance'
    session['inventory'] = []
    session['health'] = 100  # Initialize health

# Add detailed implementations for each function...
