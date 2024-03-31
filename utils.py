# Example utility functions for managing health and checking game state
def adjust_health(session, amount):
    session['health'] += amount
    if session['health'] <= 0:
        return True  # Indicate game over due to health depletion
    return False

def check_win_condition(session):
    # Define win conditions, e.g., having certain items or reaching a specific room
    pass
