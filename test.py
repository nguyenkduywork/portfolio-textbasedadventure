import unittest

import redis
import os

from game.game_logic import handle_command
from game.player import Player

from dotenv import load_dotenv

load_dotenv()


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.redis_client = redis.StrictRedis(
            host=os.getenv('HOST_IP'),
            port=int(os.getenv('REDIS_DOCKER_PORT')),
            db=0
        )
        self.test_username = 'test_account'
        self.redis_client.delete(self.test_username)

    def tearDown(self):
        self.redis_client.delete(self.test_username)
        self.redis_client.delete(f"{self.test_username}:messages")

    def test_move_north(self):
        session = {'username': self.test_username}
        player, messages = handle_command('move north', session)
        self.assertEqual(player.location, [0, 1])
        player.load_data()
        self.assertEqual(player.location, [0, 1])

    def test_move_south(self):
        session = {'username': self.test_username}
        player, messages = handle_command('move south', session)
        self.assertEqual(player.location, [0, -1])
        player.load_data()
        self.assertEqual(player.location, [0, -1])

    def test_move_east(self):
        session = {'username': self.test_username}
        player, messages = handle_command('move east', session)
        self.assertEqual(player.location, [1, 0])
        player.load_data()
        self.assertEqual(player.location, [1, 0])

    def test_move_west(self):
        session = {'username': self.test_username}
        player, messages = handle_command('move west', session)
        self.assertEqual(player.location, [-1, 0])
        player.load_data()
        self.assertEqual(player.location, [-1, 0])


if __name__ == '__main__':
    unittest.main()
