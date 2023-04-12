import os

from flask import Flask, render_template, request, redirect, session
from game.game_logic import handle_command, redis_client
from game.player import Player

from dotenv import load_dotenv
load_dotenv()

flask_secret_key = os.getenv('FLASK_SECRET')

app = Flask(__name__)
app.secret_key = flask_secret_key

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if redis_client.hget(username, 'password') == password.encode('utf-8'):
            session['username'] = username
            return redirect('/chat')
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if redis_client.hget(username, 'password'):
            return render_template('register.html', error='username already registered')
        else:
            redis_client.hset(username, mapping={'password': password})
            session['username'] = username
            player = Player(username, [0, 0])
            player.save_data()
            return redirect('/chat')
    else:
        return render_template('register.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/chat')
def chat():
    if 'username' in session:
        username = session['username']
        password = redis_client.hget(username, 'password')
        if password:
            player = Player(username, [0, 0])
            player.load_data()
            return render_template('chat.html', player=player)
        else:
            return redirect('/')
    else:
        return redirect('/')

@app.route('/command', methods=['POST'])
def handle_command_view():
    command = request.form['command'].strip().lower()
    player, messages = handle_command(command, session)

    return render_template('chat.html', player=player, messages=messages)


if __name__ == '__main__':
    app.run(debug=True)
