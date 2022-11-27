import json
import requests
import sys

import lorem

from termcolor import colored
from random_address import real_random_address
from faker import Faker

class Address():
    def __init__(self):
        fake = Faker()
        add = real_random_address()
        self.city = add['city']
        self.line1 = add['address1']
        self.line2 = add['address2']
        self.postalCode = add['postalCode']
        self.region = add['state']

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
                sort_keys=True, indent=4)

class Entity:
    def __init__(self, entity_type):
        fake = Faker()
        self.name = fake.company() + ' ' + fake.company_suffix()
        self._entity_type = entity_type
        self.description = fake.catch_phrase() + '. ' + lorem.paragraph()
        self.address = Address()
        # self.mainPhone = fake.phone_number()

    def toJSON(self):
        delattr(self, '_entity_type')
        return json.dumps(self, default=lambda o: o.__dict__, 
                sort_keys=True, indent=4)

class YextClient:
    def __init__(self, api_key, universe):
        self.v = '20220101'
        self.headers = {'Content-type': 'application/json'}
        self.universe= universe
        self.api_key = api_key 
        self.base_url = f'https://{universe}.yext.com/v2/accounts/me/entities'

    def post(self, data):
        self.final_url = self.base_url + f'?v=20220101&entityType={data._entity_type}&api_key={self.api_key}'
        # Gotcha: toJSON must be called after entity type is taken from data object - yes, this is bad
        json = data.toJSON()
        r = requests.post(self.final_url, data=json, headers=self.headers)
        print('--------------------------')
        print(f'POST {self.final_url}')
        print(f'STATUS: {r.status_code}')
        print(f'API RESPONSE: {r.json()}')
        print('--------------------------')

def create_entities(num, entity_type, client):
    for i in range(num):
        ent = Entity(entity_type)
        client.post(ent)

def main():
    # Get API Key
    api_key = input(colored('Input an API key with read/write KG permissions:\n', 'green'))

    # Select API Universe
    print(colored('Choose a Yext universe:\n 1. Production \n 2. Sandbox', 'green'))
    universe_selection = input('')
    universe = ''
    if universe_selection == '1':
        universe = 'api'
    elif universe_selection == '2':
        universe = 'api-sandbox'
    else: 
        raise Exception(colored('User Error: Please input 1 for Production or 2 for Sandbox', 'red'))

    # Select entities to create
    entities = input(colored('Input entities to create (<num_entities>:<entity_type>)\nExample: 2:location 1:FAQ 3:atm\n', 'green'))
            
    # Seed KG
    ents_arr = entities.split(' ')
    client = YextClient(api_key, universe)
    for elem in ents_arr:
        (num, entity_type) = elem.split(':')
        num = int(num)
        ent = Entity(entity_type).toJSON()
        create_entities(num, entity_type, client)

if __name__ == '__main__':
    main()
