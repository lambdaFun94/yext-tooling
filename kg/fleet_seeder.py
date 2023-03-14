from client import KgClient
from entities import Location

api_key = "371ba6333664664048b449c5917ecb56"

child_ids = []
with open("./sub_accounts.txt", "r") as f:
    child_ids = f.readlines()


def build_url(api_key, sub_account_id, v='20200101', environment='api'):
    return f'https://{environment}.yext.com/v2/accounts/{sub_account_id}/entities?v={v}&entityType=location&api_key={api_key}'


for elem in child_ids:
    client = KgClient(api_key, 'api', str(elem.strip()))
    loc = Location()
    client.create_entity(loc)
