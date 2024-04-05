import requests
from google.transit import gtfs_realtime_pb2

from .const import GTFSR_ENDPOINTS


def parse_gtfs_r(entity):
    if "ListFields" not in dir(entity):
        return entity
    entity_dict = {}
    for field in entity.ListFields():
        field_name = field[0].name
        if field[0].label == field[0].LABEL_REPEATED:
            field_value = [parse_gtfs_r(item) for item in field[1]]
        else:
            field_value = parse_gtfs_r(field[1])
        entity_dict[field_name] = field_value
    return entity_dict


def parse_gtfs_realtime_feed(feed):
    return [parse_gtfs_r(entity) for entity in feed.entity]


def parse_gtfs_r_binary(feed_data):
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(feed_data)
    return parse_gtfs_realtime_feed(feed)


class GTFSRClient:
    def __init__(
        self,
        api_key,
        header={
            "Cache-Control": "no-cache",
        },
    ):
        self.api_key = api_key
        self.session = requests.Session()
        self.header = header
        self.header["Ocp-Apim-Subscription-Key"] = api_key

    def get_data(self, endpoint):
        response = self.session.get(endpoint, headers=self.header)
        response.raise_for_status()
        return response.content

    def get_tram_servicealert(self):
        return self.get_data("https://data-exchange-api.vicroads.vic.gov.au/opendata/gtfsr/v1/tram/servicealert")
    
    def get_tram_tripupdates(self):
        return self.get_data("https://data-exchange-api.vicroads.vic.gov.au/opendata/gtfsr/v1/tram/tripupdates")
    
    def get_tram_vehicleposition(self):
        return self.get_data("https://data-exchange-api.vicroads.vic.gov.au/opendata/gtfsr/v1/tram/vehicleposition")
    
    def get_metrobus_tripupdates(self):
        return self.get_data("https://data-exchange-api.vicroads.vic.gov.au/opendata/v1/gtfsr/metrobus-tripupdates")
    
    def get_metrotrain_servicealerts(self):
        return self.get_data("https://data-exchange-api.vicroads.vic.gov.au/opendata/v1/gtfsr/metrotrain-servicealerts")
    
    def get_metrotrain_tripupdates(self):
        return self.get_data("https://data-exchange-api.vicroads.vic.gov.au/opendata/v1/gtfsr/metrotrain-tripupdates")
    
    def get_metrotrain_vehicleposition_updates(self):
        return self.get_data("https://data-exchange-api.vicroads.vic.gov.au/opendata/v1/gtfsr/metrotrain-vehicleposition-updates")
    
    def get_all(self):
        return [self.get_data(endpoint) for endpoint in GTFSR_ENDPOINTS]
        