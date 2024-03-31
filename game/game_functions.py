def handle_action(action, session):
    # Normalize the action string for consistent comparison
    action = action.lower().strip()

    # Ensure the game session is initialized
    if 'current_room' not in session:
        start_new_game(session)
    
    # Handle actions based on the normalized input
    if action.startswith('go to'):
        # Extract the room name directly without replacing parts of the string
        room = action[6:]  # Assuming all actions start with 'go to '
        return move_rooms(room, session)
    elif action.startswith('take'):
        item = action[5:]  # Assuming all actions start with 'take '
        return take_item(item, session)
    elif action == 'talk to gardener':
        return talk_to_gardener(session)
    
    return "You're not sure what to do."

def start_new_game(session):
    session['current_room'] = 'entrance'
    session['inventory'] = []
    session['health'] = 100  # Initialize health

def move_rooms(room, session):
    # Room movement logic simplified to use the room variable directly
    if room == 'library' and session['current_room'] != 'library':
        session['current_room'] = 'library'
        return "You move to the library. It's quiet here."
    elif room == 'garden' and session['current_room'] != 'garden':
        session['current_room'] = 'garden'
        return "You step into the garden. It's serene and beautiful."
    else:
        return "You can't move in that direction."

def take_item(item, session):
    # Item interaction logic simplified to use the item variable directly
    if item == 'flashlight' and 'flashlight' not in session['inventory']:
        session['inventory'].append('flashlight')
        return "You picked up the flashlight."
    elif item == 'key' and 'key' not in session['inventory']:
        session['inventory'].append('key')
        return "You found a rusty old key."
    else:
        return "There's nothing here to take."

def talk_to_gardener(session):
    # Dialogue logic remains unchanged
    if session['current_room'] == 'garden':
        return "The gardener tells you about a secret passage in the library."
    else:
        return "There's no one here to talk to."
