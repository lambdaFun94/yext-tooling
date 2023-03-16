import requests as re
from datetime import datetime

url = "https://api.yext.com/v2/accounts/me/resourcesapplyrequests?v=20220101&api_key=371ba6333664664048b449c5917ecb56"

ids = input('Enter the sub account ids separated by commas: ')

if ids != "":
    child_ids = ids.split(",")
else: 
    with open("./sub_accounts.txt", "r") as f:
        child_ids = f.readlines()


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
                "siteId": "site-id-" + dt_string_1,
                "siteName": "Deployed at " + dt_string,
                "repoId": "basic-locations-repo",
                "gitHubUrl": "github.com/lambdaFun94/avs-basic-locations-fork"
            }
        }
    }
    return body


for elem in child_ids:
    body = build_site_body(elem)
    r = re.post(url, json=body)
    print(r.json())
