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
    elif action == 'get hint':
        return get_hint(session)

    return handle_unknown_action(session)

def start_new_game(session):
    session['current_room'] = 'entrance'
    session['inventory'] = []
    session['health'] = 100  # Initialize health
    session['no_take_count'] = 0  # Counter to track "There's nothing here to take." occurrences
    session['no_action_count'] = 0  # Counter to track "You're not sure what to do." occurrences
    session['no_move_count'] = 0  # Counter to track "You can't move in that direction." occurrences

def move_rooms(room, session):
    # Room movement logic simplified to use the room variable directly
    if room == 'library' and session['current_room'] != 'library':
        session['current_room'] = 'library'
        return "You move to the library. It's quiet here."
    elif room == 'garden' and session['current_room'] != 'garden':
        session['current_room'] = 'garden'
        return "You step into the garden. It's serene and beautiful."
    else:
        session['no_move_count'] += 1  # Increment the count
        if session['no_move_count'] > 2:
            session['no_move_count'] = 0  # Reset count
            return get_hint(session)
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
        session['no_take_count'] += 1  # Increment the count
        if session['no_take_count'] > 2:
            session['no_take_count'] = 0  # Reset count
            return get_hint(session)
        else:
            return "There's nothing here to take."

def talk_to_gardener(session):
    # Dialogue logic remains unchanged
    if session['current_room'] == 'garden':
        return "The gardener tells you about a secret passage in the library."
    else:
        return "There's no one here to talk to."

def handle_unknown_action(session):
    session['no_action_count'] += 1
    if session['no_action_count'] > 2:
        session['no_action_count'] = 0
        return get_hint(session)
    else:
        return "You're not sure what to do."

def get_hint(session):
    current_room = session.get('current_room')

    # Example logic to provide hints based on the current room
    if current_room == 'garden':
        return "Maybe there's something hidden in the bushes. Try 'take item' to search."
    elif current_room == 'library':
        return "Try looking behind the bookshelves for hidden items."
    else:
        return "Explore your surroundings carefully to find clues."
