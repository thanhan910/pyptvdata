from hashlib import sha1
import hmac
import requests
import urllib.parse

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
    

    def get_all_routes(self, route_types: list[int] | int = None, route_name : str = None) -> dict:
        """
        Returns all the routes.
        Endpoint: /v3/routes
        """
        endpoint = '/v3/routes'
        params = []
        
        if route_types is not None:
            try:
                params.extend([f'route_types={route_type}' for route_type in route_types])
            except:
                params.append(f'route_types={route_types}')
        
        if route_name is not None:
            params.append(f'route_name={urllib.parse.quote(route_name)}')
        
        if len(params) > 0:
            endpoint += '?' + '&'.join(params)

        return self.get_data(endpoint)['routes']
    

    def get_all_route_types(self) -> dict:
        """
        Returns all the route types.
        Endpoint: /v3/route_types
        """
        return self.get_data('/v3/route_types')['route_types']
    

    def get_all_disruptions(self, route_types : list[int] | int = None, disruption_modes : list[int] | int = None, disruption_status : str = None) -> dict:
        """
        Returns all the disruptions.
        Endpoint: /v3/disruptions
        """
        endpoint = '/v3/disruptions'
        params = []
        if route_types is not None:
            try:
                params.extend([f'route_types={route_type}' for route_type in route_types])
            except:
                params.append(f'route_types={route_types}')
        
        if disruption_modes is not None:
            try:
                params.extend([f'disruption_modes={disruption_mode}' for disruption_mode in disruption_modes])
            except:
                params.append(f'disruption_modes={disruption_modes}')

        if disruption_status is not None:
            assert disruption_status in ['current', 'planned'], f"Disruption status must be one of 'current', 'planned', got {disruption_status}"
            params.append(f'disruption_status={disruption_status}')

        if len(params) > 0:
            endpoint += '?' + '&'.join(params)

        return self.get_data(endpoint)['disruptions']
    

    def get_all_disruption_modes(self) -> dict:
        """
        Returns all the disruption modes.
        Endpoint: /v3/disruptions/modes
        """
        return self.get_data('/v3/disruptions/modes')['disruption_modes']
    

    def get_all_outlets(self, max_results : int = 30) -> dict:
        """
        Returns all the outlets.
        Endpoint: /v3/outlets
        """
        return self.get_data(f'/v3/outlets?max_results={max_results}')['outlets']
    

    def get_search_results(
            self, 
            search_term : str,
            route_types : list[int] | int = None,
            latitude : float = None,
            longitude : float = None,
            max_distance : int = None,
            include_addresses : bool = None,
            include_outlets : bool = None,
            match_stop_by_suburb : bool = None,
            match_route_by_suburb : bool = None,
            match_stop_by_gtfs_stop_id : bool = None,
        ) -> dict:
        """
        Returns the search results.
        Endpoint: /v3/search/{search_term}
        """
        endpoint = f'/v3/search/{search_term}'
        params = []
        if route_types is not None:
            try:
                params.extend([f'route_types={route_type}' for route_type in route_types])
            except:
                params.append(f'route_types={route_types}')
        if latitude is not None:
            params.append(f'latitude={latitude}')

        if longitude is not None:
            params.append(f'longitude={longitude}')

        if max_distance is not None:
            params.append(f'max_distance={max_distance}')

        if include_addresses is not None:
            params.append(f"include_addresses={'true' if include_addresses else 'false'}")

        if include_outlets is not None:
            params.append(f"include_outlets={'true' if include_outlets else 'false'}")

        if match_stop_by_suburb is not None:
            params.append(f"match_stop_by_suburb={'true' if match_stop_by_suburb else 'false'}")

        if match_route_by_suburb is not None:
            params.append(f"match_route_by_suburb={'true' if match_route_by_suburb else 'false'}")

        if match_stop_by_gtfs_stop_id is not None:
            params.append(f"match_stop_by_gtfs_stop_id={'true' if match_stop_by_gtfs_stop_id else 'false'}")

        if len(params) > 0:
            endpoint += '?' + '&'.join(params)

        return self.get_data(f'/v3/search/{search_term}')
    

    def get_departures(
            self, 
            stop_id : int, 
            route_type : int, 
            route_id : int = None,
            platform_numbers : list[int] | int = None,
            direction_id : int = None,
            gtfs : bool = None,
            date_utc : str = None,
            max_results : int = None,
            include_cancelled : bool = None,
            look_backwards : bool = None,
            expand : list[str] | str = None,
            include_geopath : bool = None,
        ) -> dict:
        """
        Returns the departures at a stop.
        Endpoint: /v3/departures/route_type/{route_type}/stop/{stop_id}
        Endpoint: /v3/departures/route_type/{route_type}/stop/{stop_id}/route/{route_id}
        """
        endpoint = f'/v3/departures/route_type/{route_type}/stop/{stop_id}'
        if route_id is not None:
            endpoint += f'/route/{route_id}'

        params = []
        if platform_numbers is not None:
            try:
                params.extend([f'platform_numbers={platform_number}' for platform_number in platform_numbers])
            except:
                params.append(f'platform_numbers={platform_numbers}')

        if direction_id is not None:
            params.append(f'direction_id={direction_id}')

        if gtfs is not None:
            params.append(f'gtfs={'true' if gtfs else 'false'}')

        if date_utc is not None:
            params.append(f'date_utc={date_utc}')

        if max_results is not None:
            params.append(f'max_results={max_results}')

        if include_cancelled is not None:
            params.append(f'include_cancelled={'true' if include_cancelled else 'false'}')

        if look_backwards is not None:
            params.append(f'look_backwards={'true' if look_backwards else 'false'}')

        if expand is not None:
            try:
                params.extend([f'expand={expand_item}' for expand_item in expand])
            except:
                params.append(f'expand={expand}')

        if include_geopath is not None:
            params.append(f'include_geopath={'true' if include_geopath else 'false'}')

        if len(params) > 0:
            endpoint += '?' + '&'.join(params)

        return self.get_data(endpoint)
    

    def get_disruptions(
            self, 
            route_id : int = None, 
            stop_id : int = None,
            disruption_status : str = None,
        ) -> dict:
        """
        Returns the disruptions, either for a route or a stop, or both.
        Endpoint: /v3/disruptions
        Endpoint: /v3/disruptions/route/{route_id}
        Endpoint: /v3/disruptions/stop/{stop_id}
        Endpoint: /v3/disruptions/route/{route_id}/stop/{stop_id}
        """
        endpoint = '/v3/disruptions'
        
        if route_id is not None:
            endpoint += f'/route/{route_id}'
        
        if stop_id is not None:
            endpoint += f'/stop/{stop_id}'
        
        if disruption_status is not None:
            assert disruption_status in ['current', 'planned'], f"Disruption status must be one of 'current', 'planned', got {disruption_status}"
            endpoint += f'?disruption_status={disruption_status}'

        return self.get_data(endpoint)
    

    def get_disruption_info(self, disruption_id : int) -> dict:
        """
        Returns the information about a disruption.
        Endpoint: /v3/disruptions/{disruption_id}
        """
        return self.get_data(f'/v3/disruptions/{disruption_id}')
    

    def get_fare_estimate(
            self, 
            min_zone : int, 
            max_zone : int,
            journey_touch_on_utc : str = None,
            journey_touch_off_utc : str = None,
            is_journey_in_free_tram_zone : bool = None,
            travelled_route_types : list[int] | int = None,
        ) -> dict:
        """
        Returns the fare estimate between two zones.
        Endpoint: /v3/fare_estimate/min_zone/{min_zone}/max_zone/{max_zone}

        Parameters:
        - journey_touch_on_utc: The time the journey touches on in UTC. Format: yyyy-M-d h:m
        - journey_touch_off_utc: The time the journey touches off in UTC. Format: yyyy-M-d h:m
        - is_journey_in_free_tram_zone: Whether the journey is in the free tram zone.
        - travelled_route_types: The route types travelled. If more than one, use a list.
        """
        endpoint = f'/v3/fare_estimate/min_zone/{min_zone}/max_zone/{max_zone}'
        params = []

        if journey_touch_on_utc is not None:
            params.append(f'journey_touch_on_utc={urllib.parse.quote(journey_touch_on_utc)}')

        if journey_touch_off_utc is not None:
            params.append(f'journey_touch_off_utc={urllib.parse.quote(journey_touch_off_utc)}')

        if is_journey_in_free_tram_zone is not None:
            params.append(f'is_journey_in_free_tram_zone={'true' if is_journey_in_free_tram_zone else 'false'}')

        if travelled_route_types is not None:
            try:
                params.extend([f'travelled_route_types={travelled_route_type}' for travelled_route_type in travelled_route_types])
            except:
                params.append(f'travelled_route_types={travelled_route_types}')

        if len(params) > 0:
            endpoint += '?' + '&'.join(params)

        return self.get_data(endpoint)
    

    def get_nearby_outlets(self, latitude : float, longitude : float) -> dict:
        """
        Returns the outlets near a location.
        Endpoint: /v3/outlets/location/{latitude},{longitude}
        """
        return self.get_data(f'/v3/outlets/location/{latitude},{longitude}')
    
    
    def get_route_info(
            self, 
            route_id : int,
            include_geopath : bool = None,
            geopath_utc : str = None,
        ) -> dict:
        """
        Returns the information about a route.
        Endpoint: /v3/routes/{route_id}

        Parameters:
        - include_geopath: Whether to include the geopath.
        - geopath_utc: The geopath in ISO 8601 UTC format. Format: YYYY-MM-DD HH:MM:SS.ssssss
        """ 
        endpoint = f'/v3/routes/{route_id}'
        params = []

        if include_geopath is not None:
            params.append(f'include_geopath={'true' if include_geopath else 'false'}')

        if geopath_utc is not None:
            params.append(f'geopath_utc={urllib.parse.quote(geopath_utc)}')

        if len(params) > 0:
            endpoint += '?' + '&'.join(params)

        return self.get_data(endpoint)
    
    
    def get_route_directions(
            self, 
            route_id : int,
        ) -> dict:
        """
        Returns the directions of a route.
        Endpoint: /v3/directions/route/{route_id}
        """
        endpoint = f'/v3/directions/route/{route_id}'

        return self.get_data(endpoint)
    
    
    def get_route_runs(
            self, 
            route_id : int, 
            route_type : int = None,
            expand : list[str] | str = None,
            date_utc : str = None,
        ) -> dict:
        """
        Returns the runs of a route.
        Endpoint: /v3/runs/route/{route_id}
        Endpoint: /v3/runs/route/{route_id}/route_type/{route_type}
        """
        endpoint = f'/v3/runs/route/{route_id}'
        if route_type is not None:
            endpoint += f'/route_type/{route_type}'

        params = []

        if expand is not None:
            try:
                params.extend([f'expand={expand_item}' for expand_item in expand])
            except:
                params.append(f'expand={expand}')

        if date_utc is not None:
            params.append(f'date_utc={urllib.parse.quote(date_utc)}')

        if len(params) > 0:
            endpoint += '?' + '&'.join(params)

        return self.get_data(endpoint)
    
    
    def get_route_stops(
            self, 
            route_id : int, 
            route_type : int,
            direction_id : int = None,
            stop_disruptions : bool = None,
            include_geopath : bool = None,
            geopath_utc : str = None,
        ) -> dict:
        """
        Returns the stops of a route.
        Endpoint: /v3/stops/route/{route_id}/route_type/{route_type}
        """
        endpoint = f'/v3/stops/route/{route_id}/route_type/{route_type}'
        params = []

        if direction_id is not None:
            params.append(f'direction_id={direction_id}')

        if stop_disruptions is not None:
            params.append(f'stop_disruptions={'true' if stop_disruptions else 'false'}')

        if include_geopath is not None:
            params.append(f'include_geopath={'true' if include_geopath else 'false'}')

        if geopath_utc is not None:
            params.append(f'geopath_utc={urllib.parse.quote(geopath_utc)}')

        if len(params) > 0:
            endpoint += '?' + '&'.join(params)

        return self.get_data(endpoint)
    
    
    def get_direction_info(
            self, 
            direction_id : int, 
            route_type : int = None
        ) -> dict:
        """
        Returns the direction info.
        Endpoint: /v3/directions/{direction_id}
        Endpoint: /v3/directions/{direction_id}/route_type/{route_type}
        """
        endpoint = f'/v3/directions/{direction_id}'
        if route_type is not None:
            endpoint += f'/route_type/{route_type}'

        return self.get_data(endpoint)
    
    
    def get_run_info(
            self, 
            run_ref : int, 
            route_type : int = None,
            expand : list[str] | str = None,
            date_utc : str = None,
            include_geopath : bool = None,
        ) -> dict:
        """
        Returns the information about a run.
        Endpoint: /v3/runs/{run_ref}
        Endpoint: /v3/runs/{run_ref}/route_type/{route_type}
        """
        endpoint = f'/v3/runs/{run_ref}'
        if route_type is not None:
            endpoint += f'/route_type/{route_type}'

        params = []

        if expand is not None:
            try:
                params.extend([f'expand={expand_item}' for expand_item in expand])
            except:
                params.append(f'expand={expand}')

        if date_utc is not None:
            params.append(f'date_utc={urllib.parse.quote(date_utc)}')

        if include_geopath is not None:
            params.append(f'include_geopath={'true' if include_geopath else 'false'}')

        if len(params) > 0:
            endpoint += '?' + '&'.join(params)

        return self.get_data(endpoint)
    
    
    def get_stop_info(
            self, 
            stop_id : int, 
            route_type : int,
            stop_location : bool = None,
            stop_amenities : bool = None,
            stop_accessibility : bool = None,
            stop_contact : bool = None,
            stop_ticket : bool = None,
            gtfs : bool = None,
            stop_staffing : bool = None,
            stop_disruptions : bool = None,
        ) -> dict:
        """
        Returns the information about a stop.
        Endpoint: /v3/stops/{stop_id}/route_type/{route_type}
        """
        endpoint = f'/v3/stops/{stop_id}/route_type/{route_type}'

        params = []
        if stop_location is not None:
            params.append(f'stop_location={'true' if stop_location else 'false'}')

        if stop_amenities is not None:
            params.append(f'stop_amenities={'true' if stop_amenities else 'false'}')

        if stop_accessibility is not None:
            params.append(f'stop_accessibility={'true' if stop_accessibility else 'false'}')

        if stop_contact is not None:
            params.append(f'stop_contact={'true' if stop_contact else 'false'}')

        if stop_ticket is not None:
            params.append(f'stop_ticket={'true' if stop_ticket else 'false'}')

        if gtfs is not None:
            params.append(f'gtfs={'true' if gtfs else 'false'}')

        if stop_staffing is not None:
            params.append(f'stop_staffing={'true' if stop_staffing else 'false'}')

        if stop_disruptions is not None:
            params.append(f'stop_disruptions={'true' if stop_disruptions else 'false'}')

        if len(params) > 0:
            endpoint += '?' + '&'.join(params)

        return self.get_data(endpoint)
    

    
    def get_nearby_stops(
            self, 
            latitude : float, 
            longitude : float,
            route_types : list[int] | int = None,
            max_results : int = None,
            max_distance : int = None,
            stop_disruptions : bool = None,
        ) -> dict:
        """
        Returns the stops near a location.
        Endpoint: /v3/stops/location/{latitude},{longitude}
        """
        endpoint = f'/v3/stops/location/{latitude},{longitude}'
        params = []
        
        if route_types is not None:
            try:
                params.extend([f'route_types={route_type}' for route_type in route_types])
            except:
                params.append(f'route_types={route_types}')

        if max_results is not None:
            params.append(f'max_results={max_results}')

        if max_distance is not None:
            params.append(f'max_distance={max_distance}')

        if stop_disruptions is not None:
            params.append(f'stop_disruptions={'true' if stop_disruptions else 'false'}')

        if len(params) > 0:
            endpoint += '?' + '&'.join(params)

        return self.get_data(endpoint)
    
