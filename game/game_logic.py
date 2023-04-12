import redis
import os

from game.player import Player

from dotenv import load_dotenv
load_dotenv()

docker_port = int(os.getenv('REDIS_DOCKER_PORT'))
docker_redis_pw = os.getenv('REDIS_DOCKER_PW')

# redis_client = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
redis_client = redis.StrictRedis(host='127.0.0.1', port=docker_port, db=0, password=docker_redis_pw)

messages = []  # Initialize messages list outside handle_command

def handle_command(command, session):
    global messages

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

    return player, messages
