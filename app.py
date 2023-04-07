from flask import Flask, render_template, request, redirect, session
from game.player import Player
import redis

app = Flask(__name__)
app.secret_key = 'mysecretkey'

redis_client = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)


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
def handle_command():
    messages = []
    command = request.form['command'].strip().lower()
    username = session['username']
    player = Player(username, [0, 0])
    player.load_data()

    if command == 'move north':
        player.location[1] += 1
        player.save_data()
        message = 'You have moved north.'
    elif command == 'move south':
        player.location[1] -= 1
        player.save_data()
        message = 'You have moved south.'
    elif command == 'move east':
        player.location[0] += 1
        player.save_data()
        message = 'You have moved east.'
    elif command == 'move west':
        player.location[0] -= 1
        player.save_data()
        message = 'You have moved west.'
    else:
        message = 'Invalid command.'

    # Add the new message to the list
    messages.append((username, message))

    # Only keep the last 15 messages in the list
    if len(messages) > 15:
        messages = messages[-15:]

    return render_template('chat.html', player=player, messages=messages)


if __name__ == '__main__':
    # Debugging code to print all usernames and passwords in Redis
    print('---DEBUG INFO: ALL USERNAMES AND PASSWORDS IN REDIS---')
    for key in redis_client.keys('*'):
        username = key.decode('utf-8')
        password = redis_client.hget(username, 'password').decode('utf-8')
        print(f'Username: {username}, Password: {password}')

    app.run(debug=True)
