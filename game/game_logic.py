import redis
import os
from game.player import Player
from dotenv import load_dotenv

load_dotenv()

docker_port = int(os.getenv('REDIS_DOCKER_PORT'))
host_ip = os.getenv('HOST_IP')

redis_client = redis.StrictRedis(host=host_ip, port=docker_port, db=0)

data = {
    (0, 0): {
        'name': 'Town Square',
        'description': 'You are standing in the middle of a small town square. There is a fountain in the center of the square, everything else is surrounded by a forest.'
    },
    (0, 1): {
        'name': 'Central Park',
        'description': 'You are standing in the middle of a large park. You see children playing in the distance.'
    },
    (1, 1): {
        'name': 'The Playground',
        'description': 'You are standing in a playground. There are children playing on the swings and slides.'
    },
    (1, 0): {
        'name': 'The Forest',
        'description': 'You are standing in a forest. It is dark and you can hear the sounds of animals in the distance.'
    },
    (0, -1): {
        'name': 'The Lake',
        'description': 'You are standing on the shore of a large lake. The water is calm and you can see fish swimming in the water.'
    },
    (-1, -1): {
        'name': 'The Mountains',
        'description': 'You are standing at the base of a large mountain. The mountain is covered in snow and you can see a small cabin at the top.'
    },
    (-1, 0): {
        'name': 'The River',
        'description': 'You are standing on the shore of a large river. The water is flowing quickly to the lake at (0,-1).'
    },
    (-1, -2): {
        'name': 'Small Cabin Front Door',
        'description': 'You are standing in front of a small cabin. There is smoke coming from the chimney. You feel cold and tired. You should go inside. (-2,-2)'
    },
    (-2, -2): {
        'name': 'Small Cabin (Interior)',
        'description': 'You are standing in a small cabin. There is a fire burning in the fireplace. You feel warm and safe. You fell asleep.'
    }
}


def handle_command(command, session):
    username = session['username']
    player = Player(username, [0, 0])  # Use a mutable list for the location attribute
    player.load_data()

    if command == 'move north':
        player.location[1] += 1
        player.save_data()
        message = f"{username}: {command}"
        print(tuple(player.location))
        if tuple(player.location) in data:
            response = f'Server: You have moved north. You are now at {data[tuple(player.location)]["name"]}. {data[tuple(player.location)]["description"]}'
        else:
            response = f'Server: You have moved north. You are now in an unknown location.'
    elif command == 'move south':
        player.location[1] -= 1
        player.save_data()
        message = f"{username}: {command}"
        if tuple(player.location) in data:
            response = f'Server: You have moved south. You are now at {data[tuple(player.location)]["name"]}. {data[tuple(player.location)]["description"]}'
        else:
            response = f'Server: You have moved south. You are now in an unknown location.'
    elif command == 'move east':
        player.location[0] += 1
        player.save_data()
        message = f"{username}: {command}"
        if tuple(player.location) in data:
            response = f'Server: You have moved east. You are now at {data[tuple(player.location)]["name"]}. {data[tuple(player.location)]["description"]}'
        else:
            response = f'Server: You have moved east. You are now in an unknown location.'
    elif command == 'move west':
        player.location[0] -= 1
        player.save_data()
        message = f"{username}: {command}"
        if tuple(player.location) in data:
            response = f'Server: You have moved west. You are now at {data[tuple(player.location)]["name"]}. {data[tuple(player.location)]["description"]}'
        else:
            response = f'Server: You have moved west. You are now in an unknown location.'
    elif command == 'where':
        message = f"{username}: {command}"
        response = f'Server: You are currently at {data[tuple(player.location)]["name"]}. {data[tuple(player.location)]["description"]}'
    elif command == 'map':
        message = f"{username}: {command}"
        response = f'Server: You are currently at {data[tuple(player.location)]["name"]}. {data[tuple(player.location)]["description"]}. Interesting locations:'
        interesting_locations = []
        for key in data:
            if key != tuple(player.location):  # Exclude the current location from the list of interesting locations
                interesting_locations.append(f'{data[key]["name"]} is at {key}')
        response += '\n'.join(interesting_locations)
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
