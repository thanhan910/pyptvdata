from hashlib import sha1
import hmac
import requests

def get_ptv_api_url(
        endpoint : str,
        dev_id : str | int, 
        api_key : str | int,
    ):
    """
    Returns the URL to use PTV TimeTable API.

    Generates a signature from dev id (user id), API key, and endpoint.

    See the following for more information:
    - Home page: https://www.ptv.vic.gov.au/footer/data-and-reporting/datasets/ptv-timetable-api/
    - Swagger UI: https://timetableapi.ptv.vic.gov.au/swagger/ui/index
    - Swagger Docs JSON: https://timetableapi.ptv.vic.gov.au/swagger/docs/v3 (You can use this to find the endpoints you want to use.)
    """
    assert endpoint.startswith('/'), f'Endpoint must start with /, got {endpoint}'
    raw = f'{endpoint}{'&' if '?' in endpoint else '?'}devid={dev_id}'
    hashed = hmac.new(api_key.encode('utf-8'), raw.encode('utf-8'), sha1)  # Encode the raw string to bytes
    signature = hashed.hexdigest()
    return f'https://timetableapi.ptv.vic.gov.au{raw}&signature={signature}'


class PTVAPIClient:
    def __init__(self, dev_id : str | int, api_key : str | int):
        self.dev_id = dev_id
        self.api_key = api_key
        self.session = requests.Session()

    def get_data(self, endpoint : str, need_auth : bool = True):
        """
        Returns the data from the URL.
        """
        if need_auth:
            url = get_ptv_api_url(endpoint, self.dev_id, self.api_key)
        else:
            url = f'https://timetableapi.ptv.vic.gov.au{endpoint}'
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()
    

class PTVAPI3(PTVAPIClient):
    def __init__(self, dev_id : str | int, api_key : str | int):
        super().__init__(dev_id, api_key)
        
    def get_docs(self) -> dict:
        return self.get_data('/swagger/docs/v3', need_auth=False)
    
    def get_routes(self) -> dict:
        return self.get_data('/v3/routes')['routes']
    
    def get_route_types(self) -> dict:
        return self.get_data('/v3/route_types')['route_types']
    
    def get_disruptions(self) -> dict:
        return self.get_data('/v3/disruptions')['disruptions']
    
    def get_disruption_modes(self) -> dict:
        return self.get_data('/v3/disruptions/modes')['disruption_modes']
    
    def get_outlets(self) -> dict:
        return self.get_data('/v3/outlets')['outlets']

