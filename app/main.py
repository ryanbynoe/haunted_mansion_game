from flask import Flask, request, render_template, session
# Assuming game.game_functions and utils modules are correctly set up
from game.game_functions import handle_action
from utils import adjust_health, check_win_condition

app = Flask(__name__, template_folder='../templates')
app.secret_key = 'your_secret_key'  # Needed for session management

@app.route('/', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        action = request.form.get('action')
        response = handle_action(action, session)
    else:
        session.clear()  # Start a new game session, initializing necessary session variables
        session['current_room'] = 'entrance'
        session['inventory'] = []
        session['health'] = 100
        response = "You stand at the entrance of the Haunted Mansion. Where will you go?"
    
    return render_template('game.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
