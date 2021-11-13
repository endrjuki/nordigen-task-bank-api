import json
import requests
from BearerAuth import BearerAuth


with open("configuration.json") as configuration:
    cfg = json.load(configuration)

class Accounts:
    endpoint_root = cfg["accounts_endpoint"]

    @classmethod
    def retrieve_accounts_ids(self, access_token, with_balance=False):
        accounts_response = self.__retrieve_accounts_response(access_token, with_balance)
        account_ids = list(map(self.__map_to_id, accounts_response))
        return account_ids    

    @classmethod
    def __retrieve_accounts_response(self, access_token, with_balance=False):
        endpoint = f'{self.endpoint_root}'           
        query_params = { 'withBalance': "true" if with_balance else "false"}        

        response = requests.get(endpoint, params=query_params, auth=BearerAuth(access_token))
        accounts = json.loads(response.text)
        return accounts["accounts"]

    @classmethod
    def __map_to_id(self, account_entry):
        return account_entry["resourceId"]
