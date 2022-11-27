from termcolor import colored

from cli import CLI

if __name__ == '__main__':
    cli = CLI()
    while True:
        utility = input(colored('Would you like to do?\n1. Seed KG\n2. Get All Entities\n3. Get Entity\n4. Delete Entity\n', 'green'))
        if utility == '1':
            cli.seed_kg()
        elif utility == '2':
            cli.get_all_entities()
        elif utility == '3':
            ent_id = input(colored('Input Entity ID\n', 'green'))
            cli.get_entity(ent_id)
        elif utility == '4':
            ent_id = input(colored('Input Entity ID\n', 'green'))
            cli.del_entity(ent_id)
