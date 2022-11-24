import json
import requests
import sys

import lorem

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
        self.mainPhone = fake.phone_number()

    def toJSON(self):
        delattr(self, '_entity_type')
        return json.dumps(self, default=lambda o: o.__dict__, 
                sort_keys=True, indent=4)

class YextClient:
    def __init__(self, api_key='13677d5b5abd829eeec5f672db6c6858', universe ='sandbox'):
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

def create_entities(num, entity_type):
    client = YextClient()
    for i in range(num):
        ent = Entity(entity_type)
        client.post(ent)

def main():
    for i in range(len(sys.argv) - 1): 
        elem = sys.argv[i + 1]
        (num, entity_type) = elem.split(':')
        num = int(num)
        ent = Entity(entity_type).toJSON()
        create_entities(num, entity_type)

main()
