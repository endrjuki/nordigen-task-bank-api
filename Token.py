import json, requests

with open("configuration.json") as configuration:
    cfg = json.load(configuration)

class Token:
    endpoint_root = cfg["token_endpoint"]        

    @classmethod
    def get_access_token(self, SSN):
        request_body = self.__generate_request_body(SSN)
        response = json.loads(requests.post(self.endpoint_root, request_body).text)
        access_token = response["access_token"]
        return access_token        
        
    @classmethod
    def __generate_request_body(self, SSN):
        request_body = {
            "grant_type": "client_credentials",
            "client_id": cfg["client_id"],
            "client_secret": cfg["client_secret"],
            "scope": f'psd2_sandbox:{SSN}'
        }
        return request_body