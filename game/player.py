import os
import redis

from dotenv import load_dotenv
load_dotenv()

docker_port = int(os.getenv('REDIS_DOCKER_PORT'))
host_ip = os.getenv('HOST_IP')

class Player:
    def __init__(self, email, location):
        self.email = email
        self.location = location

        # self.redis_client = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        self.redis_client = redis.StrictRedis(host=host_ip, port=docker_port, db=0)

    def load_data(self):
        player_data = self.redis_client.hgetall(self.email)
        if player_data:
            if b'x' in player_data:
                x = int(player_data[b'x'].decode('utf-8'))
            else:
                x = 0
            if b'y' in player_data:
                y = int(player_data[b'y'].decode('utf-8'))
            else:
                y = 0
            self.location = [x, y]

    def save_data(self):
        self.redis_client.hset(self.email, mapping={'x': self.location[0], 'y': self.location[1]})
