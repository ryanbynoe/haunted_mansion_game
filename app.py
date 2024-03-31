# app.py
from flask import Flask, request, render_template
from your_game_module import main_game_function  # Adapt this import to your game structure

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        # Handle your game input and logic here
        action = request.form.get('action')
        game_response = main_game_function(action)  # Adapt this call to your game logic
        return render_template('game.html', response=game_response)
    return render_template('game.html', response="Welcome to the Haunted Mansion!")

if __name__ == '__main__':
    app.run(debug=True)
