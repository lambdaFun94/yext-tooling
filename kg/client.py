import requests


class KgClient:

    def __init__(self, api_key, universe, account_id='me'):
        self.headers = {'Content-type': 'application/json'}
        self.params = {'v': '20220101', 'api_key': api_key}
        self.base_url = f'https://{universe}.yext.com/v2/accounts/{account_id}/entities'

    def create_entity(self, entity):
        for k, v in entity.query_params.items():
            self.params[k] = v
        # toJSON must be called after entity type is taken from data object: bad code :(
        json = entity.toJSON()
        r = requests.post(self.base_url,
                          data=json,
                          headers=self.headers,
                          params=self.params)
        print('--------------------------')
        print(f'POST {r.url}')
        print(f'STATUS: {r.status_code}')
        print(f'API RESPONSE: {r.json()}')
        print('--------------------------')

    def get_all_entities(self):
        return requests.get(self.base_url, params=self.params)

    def get_entity(self, ent_id):
        get_ent_url = self.base_url + f'/{ent_id}'
        return requests.get(get_ent_url, params=self.params)

    def del_entity(self, ent_id):
        del_ent_url = self.base_url + f'/{ent_id}'
        return requests.delete(del_ent_url, params=self.params)
