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
        """
        Returns the Swagger docs.
        Endpoint: /swagger/docs/v3
        """
        return self.get_data('/swagger/docs/v3', need_auth=False)
    
    def get_all_routes(self) -> dict:
        """
        Returns all the routes.
        Endpoint: /v3/routes
        """
        return self.get_data('/v3/routes')['routes']
    
    def get_all_route_types(self) -> dict:
        """
        Returns all the route types.
        Endpoint: /v3/route_types
        """
        return self.get_data('/v3/route_types')['route_types']
    
    def get_all_disruptions(self) -> dict:
        """
        Returns all the disruptions.
        Endpoint: /v3/disruptions
        """
        return self.get_data('/v3/disruptions')['disruptions']
    
    def get_all_disruption_modes(self) -> dict:
        """
        Returns all the disruption modes.
        Endpoint: /v3/disruptions/modes
        """
        return self.get_data('/v3/disruptions/modes')['disruption_modes']
    
    def get_all_outlets(self) -> dict:
        """
        Returns all the outlets.
        Endpoint: /v3/outlets
        """
        return self.get_data('/v3/outlets')['outlets']
    
    def get_search_results(self, search_term : str) -> dict:
        """
        Returns the search results.
        Endpoint: /v3/search/{search_term}
        """
        return self.get_data(f'/v3/search/{search_term}')
    
    def get_departures(self, stop_id : int, route_type : int, route_id : int = None) -> dict:
        """
        Returns the departures at a stop.
        Endpoint: /v3/departures/route_type/{route_type}/stop/{stop_id}
        Endpoint: /v3/departures/route_type/{route_type}/stop/{stop_id}/route/{route_id}
        """
        if route_id:
            return self.get_data(f'/v3/departures/route_type/{route_type}/stop/{stop_id}/route/{route_id}')
        return self.get_data(f'/v3/departures/route_type/{route_type}/stop/{stop_id}')
    
    def get_disruptions(self, route_id : int = None, stop_id : int = None) -> dict:
        """
        Returns the disruptions, either for a route or a stop, or both.
        Endpoint: /v3/disruptions
        Endpoint: /v3/disruptions/route/{route_id}
        Endpoint: /v3/disruptions/stop/{stop_id}
        Endpoint: /v3/disruptions/route/{route_id}/stop/{stop_id}
        """
        if route_id is None and stop_id is None:
            return self.get_data('/v3/disruptions')
        if route_id is None:
            return self.get_data(f'/v3/disruptions/stop/{stop_id}')
        if stop_id is None:
            return self.get_data(f'/v3/disruptions/route/{route_id}')
        return self.get_data(f'/v3/disruptions/route/{route_id}/stop/{stop_id}')
    
    def get_disruption_info(self, disruption_id : int) -> dict:
        """
        Returns the information about a disruption.
        Endpoint: /v3/disruptions/{disruption_id}
        """
        return self.get_data(f'/v3/disruptions/{disruption_id}')
    
    def get_fare_estimate(self, min_zone : int, max_zone : int) -> dict:
        """
        Returns the fare estimate between two zones.
        Endpoint: /v3/fare_estimate/min_zone/{min_zone}/max_zone/{max_zone}
        """
        return self.get_data(f'/v3/fare_estimate/min_zone/{min_zone}/max_zone/{max_zone}')
    
    def get_nearby_outlets(self, latitude : float, longitude : float) -> dict:
        """
        Returns the outlets near a location.
        Endpoint: /v3/outlets/location/{latitude},{longitude}
        """
        return self.get_data(f'/v3/outlets/location/{latitude},{longitude}')
    
    def get_route_info(self, route_id : int) -> dict:
        """
        Returns the information about a route.
        Endpoint: /v3/routes/{route_id}
        """
        return self.get_data(f'/v3/routes/{route_id}')
    
    def get_route_directions(self, route_id : int) -> dict:
        """
        Returns the directions of a route.
        Endpoint: /v3/directions/route/{route_id}
        """
        return self.get_data(f'/v3/directions/route/{route_id}')
    
    def get_route_runs(self, route_id : int, route_type : int = None) -> dict:
        """
        Returns the runs of a route.
        Endpoint: /v3/runs/route/{route_id}
        Endpoint: /v3/runs/route/{route_id}/route_type/{route_type}
        """
        if route_type:
            return self.get_data(f'/v3/runs/route/{route_id}/route_type/{route_type}')
        return self.get_data(f'/v3/runs/route/{route_id}')
    
    def get_route_stops(self, route_id : int, route_type : int) -> dict:
        """
        Returns the stops of a route.
        Endpoint: /v3/stops/route/{route_id}/route_type/{route_type}
        """
        return self.get_data(f'/v3/stops/route/{route_id}/route_type/{route_type}')
    
    def get_direction_info(self, direction_id : int, route_type : int = None) -> dict:
        """
        Returns the direction info.
        Endpoint: /v3/directions/{direction_id}
        Endpoint: /v3/directions/{direction_id}/route_type/{route_type}
        """
        if route_type:
            return self.get_data(f'/v3/directions/{direction_id}/route_type/{route_type}')
        return self.get_data(f'/v3/directions/{direction_id}')
    
    def get_run_info(self, run_ref : int, route_type : int = None) -> dict:
        """
        Returns the information about a run.
        Endpoint: /v3/runs/{run_ref}
        Endpoint: /v3/runs/{run_ref}/route_type/{route_type}
        """
        if route_type:
            return self.get_data(f'/v3/runs/{run_ref}/route_type/{route_type}')
        return self.get_data(f'/v3/runs/{run_ref}')
    
    def get_stop_info(self, stop_id : int, route_type : int) -> dict:
        """
        Returns the information about a stop.
        Endpoint: /v3/stops/{stop_id}/route_type/{route_type}
        """
        return self.get_data(f'/v3/stops/{stop_id}/route_type/{route_type}')
    
    def get_nearby_stops(self, latitude : float, longitude : float) -> dict:
        """
        Returns the stops near a location.
        Endpoint: /v3/stops/location/{latitude},{longitude}
        """
        return self.get_data(f'/v3/stops/location/{latitude},{longitude}')
    
