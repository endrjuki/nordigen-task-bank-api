
from Accounts import Accounts
from Token import Token
from Transactions import Transactions

SAMPLE_SSN = 197301175209
SAMPLE_ACCOUNT_NUMBER = 98765432103
SAMPLE_TRANS_REF = "00000003116364886"

access_token = Token.get_access_token(SAMPLE_SSN)

# Retrieve a list of account ids based on access token, withBalance property (True, False), False by default
print(Accounts.retrieve_accounts_ids(access_token))

print()
# retrieve all transactions by access_token, status ("booked", "both")
print(Transactions.retrieve_all_transactions(access_token, "both"))

print()
#Retrieve specific transaction by access_token, account_id, transaction_ref
print(Transactions.retrieve_transaction(access_token, SAMPLE_ACCOUNT_NUMBER, SAMPLE_TRANS_REF))

# wrapper functions for 2 previous functions that generates access_token and invokes function
def generate_token_and_retrieve_all_transactions(ssn, status):
    access_token = Token.get_access_token(ssn)
    return Transactions.retrieve_all_transactions(access_token, status)
    
def generate_token_and_retrieve_transaction(ssn, account_id, transaction_ref):
    access_token = Token.get_access_token(ssn)
    return Transactions.retrieve_transaction(access_token, account_id, transaction_ref)

print()
print(generate_token_and_retrieve_all_transactions(SAMPLE_SSN, "both"))

print()
print(generate_token_and_retrieve_transaction(SAMPLE_SSN, SAMPLE_ACCOUNT_NUMBER, SAMPLE_TRANS_REF))