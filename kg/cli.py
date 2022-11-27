import sys
import json

from termcolor import colored

from seeder import seed 
from client import KgClient


class CLI:
    def __init__(self):
        # Get API Key
        self.api_key = input(colored('Input an API key with read/write KG permissions:\n', 'green'))

        # Select API Universe
        print(colored('Choose a Yext universe:\n1. Production \n2. Sandbox', 'green'))
        universe_selection = input('')
        if universe_selection == '1':
            self.universe = 'api'
        elif universe_selection == '2':
            self.universe = 'api-sandbox'
        else: 
            raise Exception(colored('User Error: Please input 1 for Production or 2 for Sandbox', 'red'))
        self.client = KgClient(self.api_key, self.universe)

    def get_all_entities(self):
        r = self.client.get_all_entities()
        print(self._pretty_response(r))

    def get_entity(self, ent_id):
        r = self.client.get_entity(ent_id)
        print(self._pretty_response(r))

    def del_entity(self, ent_id):
        r = self.client.del_entity(ent_id)
        print(self._pretty_response(r))

    def seed_kg(self):
        seed(self.api_key, self.universe)

    def _pretty_response(self, r):
        return json.dumps(r.json(), indent=4)

