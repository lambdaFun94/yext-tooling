
from termcolor import colored

from entities import Location, Hotel, FAQ, Job, HealthcareFacility, Restaurant, ATM
from client import YextClient

ENTITIES = ['hotel', 'location', 'FAQ', 'job', 'healthcareFacility', 'restaurant', 'ATM']

def _create_entities(num, entity_type, client):
    """
    To support a new entity:
    1. Make a new class in entities.py and import it into this module
    2. Add the name to the ENTITIES array 
    3. Add name to if, elif statement below
    """
    for i in range(num):
        if entity_type == 'hotel':
            ent = Hotel()
        elif entity_type == 'location':
            ent = Location()
        elif entity_type == 'FAQ':
            ent = FAQ()
        elif entity_type == 'job':
            ent = Job()
        elif entity_type == 'healthcareFacility':
            ent = HealthcareFacility()
        elif entity_type == 'restaurant':
            ent = Restaurant()
        elif entity_type == 'ATM':
            ent = ATM()
        else:
            raise Exception(f'User Error! Entity type: [{entity_type}] is not supported')

        client.post(ent)

def _seed_kg(api_key, universe, ents):
    ents_arr = ents.split(' ')
    client = YextClient(api_key, universe)
    for elem in ents_arr:
        (num, entity_type) = elem.split(':')
        num = int(num)
        _create_entities(num, entity_type, client)

def cli():
    # Get API Key
    api_key = input(colored('Input an API key with read/write KG permissions:\n', 'green'))

    # Select API Universe
    print(colored('Choose a Yext universe:\n1. Production \n2. Sandbox', 'green'))
    universe_selection = input('')
    universe = ''
    if universe_selection == '1':
        universe = 'api'
    elif universe_selection == '2':
        universe = 'api-sandbox'
    else: 
        raise Exception(colored('User Error: Please input 1 for Production or 2 for Sandbox', 'red'))

    # Select entities to create
    supported_entities = ', '.join(ENTITIES)
    line_1 = colored(f'Input entities to create (<num_entities>:<entity_type>)\nSupported Entities: ', 'green') 
    line_2 = colored(f'{supported_entities}\n', 'blue') 
    entities = input(line_1 + line_2)
         
    # Seed KG
    _seed_kg(api_key, universe, entities)
    

