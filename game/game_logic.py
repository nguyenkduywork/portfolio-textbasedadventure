import redis
import os

from game.player import Player

from dotenv import load_dotenv

load_dotenv()

docker_port = int(os.getenv('REDIS_DOCKER_PORT'))
host_ip = os.getenv('HOST_IP')

redis_client = redis.StrictRedis(host=host_ip, port=docker_port, db=0)


def handle_command(command, session):
    username = session['username']
    player = Player(username, [0, 0])
    player.load_data()

    if command == 'move north':
        player.location[1] += 1
        player.save_data()
        message = f"{username}: {command}"
        response = 'Server: You have moved north.'
    elif command == 'move south':
        player.location[1] -= 1
        player.save_data()
        message = f"{username}: {command}"
        response = 'Server: You have moved south.'
    elif command == 'move east':
        player.location[0] += 1
        player.save_data()
        message = f"{username}: {command}"
        response = 'Server: You have moved east.'
    elif command == 'move west':
        player.location[0] -= 1
        player.save_data()
        message = f"{username}: {command}"
        response = 'Server: You have moved west.'
    else:
        message = f"{username}: {command}"
        response = 'Server: Invalid command.'

    # Store the message and response in Redis with a key unique to the user
    redis_key = f"{username}:messages"
    redis_client.rpush(redis_key, message)
    redis_client.rpush(redis_key, response)

    # Only keep the last 10 messages for the user
    redis_client.ltrim(redis_key, -20, -1)

    # Retrieve all messages associated with the current user
    user_messages = redis_client.lrange(redis_key, 0, -1)

    messages = [msg.decode('utf-8') for msg in user_messages]

    return player, messages

