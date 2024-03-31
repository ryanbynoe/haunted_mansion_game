from flask import Flask, request, render_template, session
# Assuming game.game_functions and utils modules are correctly set up
from game.game_functions import handle_action, start_new_game

app = Flask(__name__, template_folder='../templates')
app.secret_key = 'your_secret_key'  # Needed for session management

@app.route('/', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        action = request.form.get('action')
        response = handle_action(action, session)
    else:
        start_new_game(session)  # Initialize session variables for a new game
        response = "You stand at the entrance of the Haunted Mansion. Where will you go?"
    
    return render_template('game.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
