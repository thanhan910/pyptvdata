from google.transit import gtfs_realtime_pb2

def parse_gtfs_r(entity):
    if 'ListFields' not in dir(entity):
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