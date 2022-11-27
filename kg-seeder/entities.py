import json
import lorem
import requests

from random_address import real_random_address
from faker import Faker

class Entity: 

    def toJSON(self):
        delattr(self, 'entity_type')
        delattr(self, 'query_params')
        return json.dumps(self, default=lambda o: o.__dict__, 
                sort_keys=True, indent=4)

class Location(Entity):
    def __init__(self, entity_type='location'):
        fake = Faker()
        self.name = fake.company() + ' ' + fake.company_suffix()
        self.entity_type = entity_type
        self.description = fake.catch_phrase() + '. ' + lorem.paragraph()
        self.address = Address()
        # self.mainPhone = fake.phone_number()

    def toJSON(self):
        delattr(self, 'entity_type')
        return json.dumps(self, default=lambda o: o.__dict__, 
                sort_keys=True, indent=4)

class Hotel(Location):
    def __init__(self):
        super().__init__('hotel')


class Address():
    def __init__(self):
        fake = Faker()
        add = real_random_address()
        self.city = add['city']
        self.line1 = add['address1']
        self.line2 = add['address2']
        self.postalCode = add['postalCode']
        self.region = add['state']

class FAQ(Entity):
    def __init__(self):
        self.entity_type = 'faq'
        self.query_params = {'format': 'html'}
        self._generate_faq()

    def _generate_faq(self):
        base_url = 'https://opentdb.com/api.php?amount=1&type=multiple'
        r = requests.get(base_url).json()['results'][0]
        self.name = r['question']
        self.answer = r['correct_answer']

