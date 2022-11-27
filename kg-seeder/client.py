import requests

class YextClient:
    def __init__(self, api_key, universe):
        self.v = '20220101'
        self.headers = {'Content-type': 'application/json'}
        self.universe = universe
        self.api_key = api_key 
        self.base_url = f'https://{universe}.yext.com/v2/accounts/me/entities?v=20220101&api_key={self.api_key}&'
        


    def post(self, data):
        self.final_url = self.base_url + f'entityType={data.entity_type}'
        if hasattr(data, 'query_params'):
            self.final_url += self._build_query_params(data.query_params)

        # Gotcha: toJSON must be called after entity type is taken from data object - yes, this is bad
        json = data.toJSON()
        r = requests.post(self.final_url, data=json, headers=self.headers)
        print('--------------------------')
        print(f'POST {self.final_url}')
        print(f'STATUS: {r.status_code}')
        print(f'API RESPONSE: {r.json()}')
        print('--------------------------')

    def _build_query_params(self, params):
        query_string = ''
        for k, v in params.items():
            query_string += f'&{k}={v}'
        return query_string



