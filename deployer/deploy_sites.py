import requests as re
import random
from datetime import datetime

url = "https://api.yext.com/v2/accounts/me/resourcesapplyrequests?v=20220101&api_key=371ba6333664664048b449c5917ecb56"
ids = input(
    'Enter sub account ids separated by commas or "s" for a subset of 6 accts: '
)

child_ids = []
if ids == "s":
    with open("./subset_accounts.txt", "r") as f:
        child_ids = f.readlines()
elif ids != "":
    child_ids = ids.split(",")
else:
    with open("./sub_accounts.txt", "r") as f:
        child_ids = f.readlines()


class DeployMessage:

    def __init__(self, json):
        print(f'''
            Site Deployed!
            Site Name: {json['response']['source']['variables']['siteName']}
            ''')


def build_site_body(sub_account_id):
    stripped = sub_account_id.strip()

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_string_1 = now.strftime("%H-%M-%S")

    body = {
        "targetAccountId": stripped,
        "source": {
            "type": "GitHub",
            "url": "https://github.com/lambdaFun94/cac-pages-yextsite-config",
            "variables": {
                "siteId":
                "site-id-" + dt_string_1 + str(random.randint(1, 100)),
                "siteName": "Andrew's SMB Site Deployed at: " + dt_string,
                "repoId": "basic-locations-repo-fleet",
                "gitHubUrl": "github.com/lambdaFun94/basic-locations-site"
            }
        }
    }
    return body


json = {
    'meta': {
        'uuid': '0187ec56-f853-61c8-186e-f35af45dcdff',
        'errors': []
    },
    'response': {
        'id': 20462,
        'targetAccountId': '6728500',
        'dateSubmitted': '2023-05-05T14:35:35',
        'source': {
            'type': 'GITHUB',
            'url': 'https://github.com/lambdaFun94/cac-pages-yextsite-config',
            'variables': {
                'siteId': 'site-id-10-35-3535',
                'siteName': 'Deployed at 05/05/2023 10:35:35',
                'repoId': 'basic-locations-repo-fleet',
                'gitHubUrl': 'github.com/lambdaFun94/basic-locations-site'
            }
        },
        'status': 'SUBMITTED'
    }
}

for elem in child_ids:
    body = build_site_body(elem)
    r = re.post(url, json=body)
    DeployMessage(r.json())
