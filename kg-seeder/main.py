from termcolor import colored

from entities import Location, Hotel, FAQ
from client import YextClient

def create_entities(num, entity_type, client):
    for i in range(num):
        if entity_type == 'hotel':
            ent = Hotel()
        elif entity_type == 'location':
            ent = Location()
        elif entity_type == 'FAQ':
            ent = FAQ()

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
        ent = Location(entity_type).toJSON()
        create_entities(num, entity_type, client)

if __name__ == '__main__':
    main()
