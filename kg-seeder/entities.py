import json
import lorem
import requests

from random_address import real_random_address
from faker import Faker


class _Entity: 

    def toJSON(self):
        if hasattr(self, 'entity_type'):
            delattr(self, 'entity_type')
        if hasattr(self, 'query_params'):
            delattr(self, 'query_params')
        return json.dumps(self, default=lambda o: o.__dict__, 
                sort_keys=True, indent=4)

class _Address():
    def __init__(self):
        fake = Faker()
        add = real_random_address()
        self.city = add['city']
        self.line1 = add['address1']
        self.line2 = add['address2']
        self.postalCode = add['postalCode']
        self.region = add['state']


class Location(_Entity):
    def __init__(self, entity_type='location'):
        fake = Faker()
        self.name = fake.company() + ' ' + fake.company_suffix()
        self.entity_type = entity_type
        self.description = fake.catch_phrase() + '. ' + lorem.paragraph()
        self.address = _Address()
        # self.mainPhone = fake.phone_number()


class Hotel(Location):
    def __init__(self):
        super().__init__('hotel')

class HealthcareFacility(Location):
    def __init__(self):
        super().__init__('healthcareFacility')

class Job(_Entity):
    def __init__(self):
        fake = Faker()
        self.entity_type = 'job'
        self.name = fake.job()
        self.description = lorem.sentence()


class FAQ(_Entity):
    def __init__(self):
        self.entity_type = 'faq'
        self.query_params = {'format': 'html'}
        self._generate_faq()

    def _generate_faq(self):
        base_url = 'https://opentdb.com/api.php?amount=1&type=multiple'
        r = requests.get(base_url).json()['results'][0]
        self.name = r['question']
        self.answer = r['correct_answer']

