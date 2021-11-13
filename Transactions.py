import json, requests
from BearerAuth import BearerAuth
from Accounts import Accounts

with open("configuration.json") as configuration:
    cfg = json.load(configuration)

class Transactions:
    endpoint_root = cfg["accounts_endpoint"] 

    @classmethod
    def retrieve_all_transactions(self, access_token, status="both"):
        all_account_ids = Accounts.retrieve_accounts_ids(access_token)
        all_transactions = []

        for account_id in all_account_ids:
            all_transactions.append(self.retrieve_account_transactions(access_token, account_id, "booked"))

        return all_transactions        

    @classmethod
    def retrieve_transaction(self, access_token, account_id, transaction_ref):
        endpoint = f'{self.endpoint_root}/{account_id}/transactions/{transaction_ref}'        
        response = requests.get(endpoint, auth=BearerAuth(access_token))
        return json.loads(response.text)

    @classmethod
    def retrieve_account_transactions(self, access_token, account_id, status="both"):
        endpoint = f'{self.endpoint_root}/{account_id}/transactions'        
        query_params = { 'status': status }
        response = requests.get(endpoint, params=query_params, auth=BearerAuth(access_token))

        transactions = json.loads(response.text)
        return transactions