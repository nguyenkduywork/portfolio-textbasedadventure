import redis
import os

from game.player import Player

from dotenv import load_dotenv
load_dotenv()

docker_port = int(os.getenv('REDIS_DOCKER_PORT'))
host_ip = os.getenv('HOST_IP')

# redis_client = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
redis_client = redis.StrictRedis(host=host_ip, port=docker_port, db=0)

def handle_command(command, session):
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

    # Store the message in Redis with a key unique to the user
    redis_key = f"{username}:messages"
    redis_client.rpush(redis_key, f"{username}: {message}")

    # Only keep the last 15 messages for the user
    redis_client.ltrim(redis_key, -15, -1)

    # Retrieve all messages associated with the current user
    user_messages = redis_client.lrange(redis_key, 0, -1)
    messages = [msg.decode('utf-8').split(": ") for msg in user_messages]

    return messages


