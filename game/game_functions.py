def handle_action(action, session):
    if 'current_room' not in session:
        start_new_game(session)
    
    if action.startswith('go to'):
        return move_rooms(action, session)
    elif action.startswith('take'):
        return take_item(action, session)
    elif action == 'talk to gardener':
        return talk_to_gardener(session)
    
    return "You're not sure what to do."

def start_new_game(session):
    session['current_room'] = 'entrance'
    session['inventory'] = []
    session['health'] = 100  # Initialize health

def move_rooms(action, session):
    # Example room navigation logic
    if 'library' in action:
        session['current_room'] = 'library'
        return "You move to the library. It's quiet here."
    elif 'garden' in action:
        session['current_room'] = 'garden'
        return "You step into the garden. It's serene and beautiful."
    else:
        return "You can't move in that direction."

def take_item(action, session):
    # Example item interaction logic
    if 'flashlight' in action:
        session['inventory'].append('flashlight')
        return "You picked up the flashlight."
    elif 'key' in action:
        session['inventory'].append('key')
        return "You found a rusty old key."
    else:
        return "There's nothing here to take."

def talk_to_gardener(session):
    if session['current_room'] == 'garden':
        return "The gardener tells you about a secret passage in the library."
    else:
        return "There's no one here to talk to."
