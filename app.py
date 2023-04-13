import os

from flask import Flask, render_template, request, redirect, session
from dotenv import load_dotenv

from game.game_logic import handle_command
from game.player import Player
from game.game_logic import redis_client

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET')


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        stored_password = redis_client.hget(username, 'password')
        if stored_password and stored_password.decode('utf-8') == password:
            session['username'] = username
            return redirect('/chat')
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if redis_client.hget(username, 'password'):
            return render_template('register.html', error='Username already registered')
        else:
            redis_client.hset(username, mapping={'password': password})
            session['username'] = username
            player = Player(username, [0, 0])
            player.save_data()
            return redirect('/chat')
    else:
        return render_template('register.html')


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return redirect('/')


@app.route('/chat')
def chat():
    if 'username' in session:
        username = session['username']
        stored_password = redis_client.hget(username, 'password')
        if stored_password:
            player = Player(username, [0, 0])
            player.load_data()
            return render_template('chat.html', player=player)
        else:
            return redirect('/')
    else:
        return redirect('/')


@app.route('/command', methods=['POST'])
def handle_command_view():
    command = request.form.get('command', '').strip().lower()
    player, messages = handle_command(command, session)

    return render_template('chat.html', player=player, messages=messages)


if __name__ == '__main__':
    app.run(debug=True)
