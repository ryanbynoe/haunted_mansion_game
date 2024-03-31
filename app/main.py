from flask import Flask, request, render_template, session, jsonify
from flask_cors import CORS  # Import CORS
from game.game_functions import handle_action
from utils import adjust_health, check_win_condition

app = Flask(__name__, template_folder='../templates')
CORS(app)  # Enable CORS for all domains on all routes
app.secret_key = 'your_secret_key'  # Needed for session management

@app.route('/', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        action = request.form.get('action')
        response = handle_action(action, session)
    else:
        session.clear()  # Start a new game session
        response = "You stand at the entrance of the Haunted Mansion. Where will you go?"
    return render_template('game.html', response=response)

@app.route('/get-hints', methods=['POST'])
def get_hints():
    user_input = request.json['userInput']
    hints = generate_hints_based_on_input(user_input)
    return jsonify(hints)

def generate_hints_based_on_input(user_input):
    # Example function to generate hints. Customize this based on your game's logic.
    if "explore" in user_input.lower():
        return ["Try exploring the garden.", "Explore the library for clues."]
    return ["Not sure what to do? Try 'explore'."]

if __name__ == '__main__':
    app.run(debug=True)
