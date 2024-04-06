from dataclasses import dataclass


@dataclass
class V3Status:
    """
    
    """
    version: str
    """
    API Version number
    """
    health: int
    """
    API system health status (0=offline, 1=online)
    """

@dataclass
class V3DeparturesBroadParameters:
    """
    
    """
    platform_numbers: list[int]
    """
    Filter by platform number at stop
    """
    direction_id: int
    """
    Filter by identifier of direction of travel; values returned by Directions API - /v3/directions/route/{route_id}
    """
    gtfs: bool
    """
    Indicates that stop_id parameter will accept "GTFS stop_id" data
    """
    date_utc: str
    """
    Filter by the date and time of the request (ISO 8601 UTC format) (default = current date and time)
    """
    max_results: int
    """
    Maximum number of results returned
    """
    include_cancelled: bool
    """
    Indicates if cancelled services (if they exist) are returned (default = false) - metropolitan train only
    """
    look_backwards: bool
    """
    Indicates if filtering runs (and their departures) to those that arrive at destination before date_utc (default = false). Requires max_results &gt; 0.
    """
    expand: list[str]
    """
    List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor or None.
    Run must be expanded to receive VehiclePosition and VehicleDescriptor information.
    """
    include_geopath: bool
    """
    Indicates if the route geopath should be returned
    """

@dataclass
class V3Departure:
    """
    
    """
    stop_id: int
    """
    Stop identifier
    """
    route_id: int
    """
    Route identifier
    """
    run_id: int
    """
    Numeric trip/service run identifier. Defaults to -1 when run identifier is Alphanumeric
    """
    run_ref: str
    """
    Alphanumeric trip/service run identifier
    """
    direction_id: int
    """
    Direction of travel identifier
    """
    disruption_ids: list[int]
    """
    Disruption information identifier(s)
    """
    scheduled_departure_utc: str
    """
    Scheduled (i.e. timetabled) departure time and date in ISO 8601 UTC format
    """
    estimated_departure_utc: str
    """
    Real-time estimate of departure time and date in ISO 8601 UTC format
    """
    at_platform: bool
    """
    Indicates if the metropolitan train service is at the platform at the time of query; returns false for other modes
    """
    platform_number: str
    """
    Platform number at stop (metropolitan train only; returns null for other modes)
    """
    flags: str
    """
    Flag indicating special condition for run (e.g. RR Reservations Required, GC Guaranteed Connection, DOO Drop Off Only, PUO Pick Up Only, MO Mondays only, TU Tuesdays only, WE Wednesdays only, TH Thursdays only, FR Fridays only, SS School days only; ignore E flag)
    """
    departure_sequence: int
    """
    Chronological sequence for the departures in a run. Order ascendingly by this field to get chronological order (earliest first) of departures with the same run_ref. NOTE, this field is not always N+1 or N-1 of the previous or following departure. e.g 100, 200, 250, 300 instead of 1, 2, 3, 4
    """

@dataclass
class V3StopModel:
    """
    
    """
    stop_distance: float
    """
    Distance of stop from input location (in metres); returns 0 if no location is input
    """
    stop_suburb: str
    """
    suburb of stop
    """
    stop_name: str
    """
    Name of stop
    """
    stop_id: int
    """
    Stop identifier
    """
    route_type: int
    """
    Transport mode identifier
    """
    stop_latitude: float
    """
    Geographic coordinate of latitude at stop
    """
    stop_longitude: float
    """
    Geographic coordinate of longitude at stop
    """
    stop_landmark: str
    """
    Landmark in proximity of stop
    """
    stop_sequence: int
    """
    Sequence of the stop on the route/run; return 0 when route_id or run_id not specified. Order ascendingly by this field (when non zero) to get physical order (earliest first) of stops on the route_id/run_id.
    """

@dataclass
class V3Direction:
    """
    
    """
    direction_id: int
    """
    Direction of travel identifier
    """
    direction_name: str
    """
    Name of direction of travel
    """
    route_id: int
    """
    Route identifier
    """
    route_type: int
    """
    Transport mode identifier
    """

@dataclass
class V3VehiclePosition:
    """
    
    """
    latitude: float
    """
    Geographic coordinate of latitude of the vehicle when known. May be null.
    Only available for some bus runs.
    """
    longitude: float
    """
    Geographic coordinate of longitude of the vehicle when known. 
    Only available for some bus runs.
    """
    easting: float
    """
    CIS - Metro Train Vehicle Location Easting coordinate
    """
    northing: float
    """
    CIS - Metro Train Vehicle Location Northing coordinate
    """
    direction: str
    """
    CIS - Metro Train Vehicle Location Direction
    """
    bearing: float
    """
    Compass bearing of the vehicle when known, clockwise from True North, i.e., 0 is North and 90 is East. May be null.
    Only available for some bus runs.
    """
    supplier: str
    """
    Supplier of vehicle position data.
    """
    datetime_utc: str
    """
    Date and time that the vehicle position data was supplied.
    """
    expiry_time: str
    """
    CIS - Metro Train Vehicle Location data expiry time
    """

@dataclass
class V3VehicleDescriptor:
    """
    
    """
    operator: str
    """
    Operator name of the vehicle such as "Metro Trains Melbourne", "Yarra Trams", "Ventura Bus Line", "CDC" or "Sita Bus Lines" . May be null/empty.
    Only available for train, tram, v/line and some bus runs.
    """
    id: str
    """
    Operator identifier of the vehicle such as "26094". May be null/empty. Only available for some tram and bus runs.
    """
    low_floor: bool
    """
    Indicator if vehicle has a low floor. May be null. Only available for some tram runs.
    """
    air_conditioned: bool
    """
    Indicator if vehicle is air conditioned. May be null. Only available for some tram runs.
    """
    description: str
    """
    Vehicle description such as "6 Car Comeng", "6 Car Xtrapolis", "3 Car Comeng", "6 Car Siemens", "3 Car Siemens". May be null/empty.
    Only available for some metropolitan train runs.
    """
    supplier: str
    """
    Supplier of vehicle descriptor data.
    """
    length: str
    """
    The length of the vehicle. Applies to CIS - Metro Trains
    """

@dataclass
class V3DisruptionStop:
    """
    
    """
    stop_id: int
    """
    
    """
    stop_name: str
    """
    
    """

@dataclass
class V3DisruptionDirection:
    """
    
    """
    route_direction_id: int
    """
    Route and direction of travel combination identifier
    """
    direction_id: int
    """
    Direction of travel identifier
    """
    direction_name: str
    """
    Name of direction of travel
    """
    service_time: str
    """
    Time of service to which disruption applies, in 24 hour clock format (HH:MM:SS) AEDT/AEST; returns null if disruption applies to multiple (or no) services
    """

@dataclass
class V3DeparturesSpecificParameters:
    """
    
    """
    direction_id: int
    """
    Filter by identifier of direction of travel; values returned by Directions API - /v3/directions/route/{route_id}
    """
    gtfs: bool
    """
    Indicates that stop_id parameter will accept "GTFS stop_id" data
    """
    date_utc: str
    """
    Filter by the date and time of the request (ISO 8601 UTC format) (default = current date and time)
    """
    max_results: int
    """
    Maximum number of results returned
    """
    include_cancelled: bool
    """
    Indicates if cancelled services (if they exist) are returned (default = false) - metropolitan train only
    """
    look_backwards: bool
    """
    Indicates if filtering runs (and their departures) to those that arrive at destination before date_utc (default = false). Requires max_results &gt; 0.
    """
    expand: list[str]
    """
    List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor or None.
    Run must be expanded to receive VehiclePosition and VehicleDescriptor information.
    """
    include_geopath: bool
    """
    Indicates if the route geopath should be returned
    """

@dataclass
class V3RouteDeparturesSpecificParameters:
    """
    
    """
    train_scheduled_timetables: bool
    """
    DEPRECATED - use `scheduled_timetables` instead
    """
    scheduled_timetables: bool
    """
    When set to true, all timetable information returned by Chronos will be sourced from the scheduled timetables,
    while when set to false (default state), the operational timetables will be used where available.
    """
    date_utc: str
    """
    Filter by the date and time of the request (ISO 8601 UTC format) (default = current date and time)
    """
    max_results: int
    """
    Maximum number of results returned
    """
    include_cancelled: bool
    """
    Indicates if cancelled services (if they exist) are returned (default = false) - metropolitan train only
    """
    look_backwards: bool
    """
    Indicates if filtering runs (and their departures) to those that arrive at destination before date_utc (default = false). Requires max_results &gt; 0.
    """
    expand: list[str]
    """
    List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor or None.
    Run must be expanded to receive VehiclePosition and VehicleDescriptor information.
    """
    include_geopath: bool
    """
    Indicates if the route geopath should be returned
    """

@dataclass
class V3StopDepartureRequestRouteDirection:
    """
    
    """
    route_id: str
    """
    Identifier of route; values returned by Routes API - v3/routes
    """
    direction_id: int
    """
    Direction of travel identifier; values returned by Directions API - v3/directions
    """
    direction_name: str
    """
    Name of direction of travel; values returned by Directions API - v3/directions
    """

@dataclass
class V3BulkDeparturesStopResponse:
    """
    
    """
    stop_name: str
    """
    Name of stop
    """
    stop_id: int
    """
    Stop identifier
    """
    stop_latitude: float
    """
    Geographic coordinate of latitude at stop
    """
    stop_longitude: float
    """
    Geographic coordinate of longitude at stop
    """
    stop_suburb: str
    """
    suburb of stop
    """
    stop_landmark: str
    """
    Landmark in proximity of stop
    """

@dataclass
class V3BulkDeparturesRouteDirectionResponse:
    """
    
    """
    route_id: str
    """
    Route identifier
    """
    direction_id: int
    """
    Direction of travel identifier
    """
    direction_name: str
    """
    Name of direction of travel
    """

@dataclass
class V3DirectionWithDescription:
    """
    
    """
    route_direction_description: str
    """
    
    """
    direction_id: int
    """
    Direction of travel identifier
    """
    direction_name: str
    """
    Name of direction of travel
    """
    route_id: int
    """
    Route identifier
    """
    route_type: int
    """
    Transport mode identifier
    """

@dataclass
class V3StopBasic:
    """
    
    """
    stop_id: int
    """
    
    """
    stop_name: str
    """
    
    """

@dataclass
class V3DisruptionMode:
    """
    
    """
    disruption_mode_name: str
    """
    Name of disruption mode
    """
    disruption_mode: int
    """
    Disruption mode identifier
    """

@dataclass
class V3StopTicket:
    """
    
    """
    ticket_type: str
    """
    Indicates the ticket type for the stop (myki, paper or both)
    """
    zone: str
    """
    Description of the zone
    """
    is_free_fare_zone: bool
    """
    Indicates whether the stop is inside the free fare zone
    """
    ticket_machine: bool
    """
    
    """
    ticket_checks: bool
    """
    
    """
    vline_reservation: bool
    """
    
    """
    ticket_zones: list[int]
    """
    
    """

@dataclass
class V3OutletParameters:
    """
    
    """
    max_results: int
    """
    Maximum number of results returned (default = 30)
    """

@dataclass
class V3Outlet:
    """
    
    """
    outlet_slid_spid: str
    """
    The SLID / SPID
    """
    outlet_name: str
    """
    The location name of the outlet
    """
    outlet_business: str
    """
    The business name of the outlet
    """
    outlet_latitude: float
    """
    Geographic coordinate of latitude at outlet
    """
    outlet_longitude: float
    """
    Geographic coordinate of longitude at outlet
    """
    outlet_suburb: str
    """
    The city/municipality the outlet is in
    """
    outlet_postcode: int
    """
    The postcode for the outlet
    """
    outlet_business_hour_mon: str
    """
    The business hours on Monday
    """
    outlet_business_hour_tue: str
    """
    The business hours on Tuesday
    """
    outlet_business_hour_wed: str
    """
    The business hours on Wednesday
    """
    outlet_business_hour_thur: str
    """
    The business hours on Thursday
    """
    outlet_business_hour_fri: str
    """
    The business hours on Friday
    """
    outlet_business_hour_sat: str
    """
    The business hours on Saturday
    """
    outlet_business_hour_sun: str
    """
    The business hours on Sunday
    """
    outlet_notes: str
    """
    Any additional notes for the outlet such as 'Buy pre-loaded myki cards only'. May be null/empty.
    """

@dataclass
class V3OutletGeolocationParameters:
    """
    
    """
    max_distance: float
    """
    Filter by maximum distance (in metres) from location specified via latitude and longitude parameters (default = 300)
    """
    max_results: int
    """
    Maximum number of results returned (default = 30)
    """

@dataclass
class V3OutletGeolocation:
    """
    
    """
    outlet_distance: float
    """
    Distance of outlet from input location (in metres); returns 0 if no location is input
    """
    outlet_slid_spid: str
    """
    The SLID / SPID
    """
    outlet_name: str
    """
    The location name of the outlet
    """
    outlet_business: str
    """
    The business name of the outlet
    """
    outlet_latitude: float
    """
    Geographic coordinate of latitude at outlet
    """
    outlet_longitude: float
    """
    Geographic coordinate of longitude at outlet
    """
    outlet_suburb: str
    """
    The city/municipality the outlet is in
    """
    outlet_postcode: int
    """
    The postcode for the outlet
    """
    outlet_business_hour_mon: str
    """
    The business hours on Monday
    """
    outlet_business_hour_tue: str
    """
    The business hours on Tuesday
    """
    outlet_business_hour_wed: str
    """
    The business hours on Wednesday
    """
    outlet_business_hour_thur: str
    """
    The business hours on Thursday
    """
    outlet_business_hour_fri: str
    """
    The business hours on Friday
    """
    outlet_business_hour_sat: str
    """
    The business hours on Saturday
    """
    outlet_business_hour_sun: str
    """
    The business hours on Sunday
    """
    outlet_notes: str
    """
    Any additional notes for the outlet such as 'Buy pre-loaded myki cards only'. May be null/empty.
    """

@dataclass
class V3RouteServiceStatus:
    """
    
    """
    description: str
    """
    
    """
    timestamp: str
    """
    
    """

@dataclass
class V3RouteType:
    """
    
    """
    route_type_name: str
    """
    Name of transport mode
    """
    route_type: int
    """
    Transport mode identifier
    """

@dataclass
class V3SearchParameters:
    """
    
    """
    route_types: list[int]
    """
    Filter by route_type; values returned via RouteTypes API (note: stops and routes are ordered by route_types specified)
    """
    latitude: float
    """
    Filter by geographic coordinate of latitude
    """
    longitude: float
    """
    Filter by geographic coordinate of longitude
    """
    max_distance: float
    """
    Filter by maximum distance (in metres) from location specified via latitude and longitude parameters
    """
    include_addresses: bool
    """
    Placeholder for future development; currently unavailable
    """
    include_outlets: bool
    """
    Indicates if outlets will be returned in response (default = true)
    """
    match_stop_by_suburb: bool
    """
    Indicates whether to find stops by suburbs in the search term (default = true)
    """
    match_route_by_suburb: bool
    """
    Indicates whether to find routes by suburbs in the search term (default = true)
    """
    match_stop_by_gtfs_stop_id: bool
    """
    Indicates whether to search for stops according to a metlink stop ID (default = false)
    """

@dataclass
class V3ResultOutlet:
    """
    
    """
    outlet_distance: float
    """
    Distance of outlet from input location (in metres); returns 0 if no location is input
    """
    outlet_slid_spid: str
    """
    The SLID / SPID
    """
    outlet_name: str
    """
    The location name of the outlet
    """
    outlet_business: str
    """
    The business name of the outlet
    """
    outlet_latitude: float
    """
    Geographic coordinate of latitude at outlet
    """
    outlet_longitude: float
    """
    Geographic coordinate of longitude at outlet
    """
    outlet_suburb: str
    """
    The city/municipality the outlet is in
    """
    outlet_postcode: int
    """
    The postcode for the outlet
    """
    outlet_business_hour_mon: str
    """
    The business hours on Monday
    """
    outlet_business_hour_tue: str
    """
    The business hours on Tuesday
    """
    outlet_business_hour_wed: str
    """
    The business hours on Wednesday
    """
    outlet_business_hour_thur: str
    """
    The business hours on Thursday
    """
    outlet_business_hour_fri: str
    """
    The business hours on Friday
    """
    outlet_business_hour_sat: str
    """
    The business hours on Saturday
    """
    outlet_business_hour_sun: str
    """
    The business hours on Sunday
    """
    outlet_notes: str
    """
    Any additional notes for the outlet such as 'Buy pre-loaded myki cards only'. May be null/empty.
    """

@dataclass
class V3SiriLineRefDirectionRefStopPointRef:
    """
    
    """
    line_ref: str
    """
    Siri LineRef
    """
    direction_ref: int
    """
    Siri DirectionRef  (in, out, up, down, clockwise, counterclockwise, Inbound, Outbound)
    """
    stop_point_ref: int
    """
    Siri StopPointRef
    """

@dataclass
class V3StopPoint:
    """
    
    """
    stop_id: int
    """
    
    """

@dataclass
class V3SiriReferenceDataDetail:
    """
    
    """
    route_id: int
    """
    
    """
    route_number_short: str
    """
    Route number
    """
    direction_id: int
    """
    
    """
    tracking_supplier_id: int
    """
    Authority (Upstream SIRI provider) of a route and direction
    """
    route_type: int
    """
    
    """

@dataclass
class V3SiriLineRef:
    """
    
    """
    line_ref: str
    """
    Siri LineRef
    """
    direction_ref: int
    """
    Siri DirectionRef  (in, out, up, down, clockwise, counterclockwise, Inbound, Outbound)
    """

@dataclass
class V3SiriLineRefDirectionRefsDictionary:
    """
    
    """
    direction_refs: list
    """
    
    """
    unmatched_direction_refs: str
    """
    
    """

@dataclass
class V3DynamoDbTimetable:
    """
    
    """
    table_name: str
    """
    Name of corresponding table in DynamoDB.
    """
    parser_version: int
    """
    Parser verison
    """
    parser_mapping_version: str
    """
    Diva Mapping Version used to load Parser into DynamoDB
    """
    pt_version: int
    """
    PT version
    """
    pt_mapping_version: str
    """
    Diva Mapping Version used to load PT into DynamoDB
    """
    transport_type: int
    """
    A.k.a. Transport Mode (e.g. Train, Tram, Bus, V/Line, Nightrider)
    """
    applicable_local_date: str
    """
    Formated date string of applicable date
    """
    exists: bool
    """
    True if the named table has been created in DynamoDB (i.e. at least one departure record has been loaded),
    or false if there are no records for this date and transport type.
    """

@dataclass
class V3SiriDownstreamSubscriptionTopic:
    """
    
    """
    line_ref: str
    """
    
    """
    direction_ref: int
    """
    
    """
    route_type: int
    """
    
    """

@dataclass
class V3SiriSubscriptionTopic:
    """
    
    """
    line_ref: str
    """
    Siri LineRef
    """
    direction_ref: int
    """
    Siri DirectionRef  (in, out, up, down, clockwise, counterclockwise, Inbound, Outbound)
    """
    route_type: int
    """
    Route Type eg. 0 (Train) 1 (Tram) 2 (Bus) 3 (Vline) 4 (NightRider)
    """

@dataclass
class V3SiriDownstreamSubscriptionResponse:
    """
    
    """
    valid_until: str
    """
    The Data Horizon of Chronos
    """

@dataclass
class V3SiriDownstreamSubscriptionDeleteRequest:
    """
    
    """
    subscriber_ref: str
    """
    Siri Subscriber Ref
    """
    subscription_ref: list[str]
    """
    Siri Subscription Reference(s) - Unique to a Subscriber Ref.
    If `null`, then all subscriptions will be terminated for the referenced Subscriber.
    """

@dataclass
class V3Void:
    """
    
    """
    pass

@dataclass
class V3StopAmenityDetails:
    """
    
    """
    toilet: bool
    """
    Indicates if there is a public toilet at or near the stop
    """
    taxi_rank: bool
    """
    Indicates if there is a taxi rank at or near the stop
    """
    car_parking: str
    """
    The number of free car parking spots at the stop
    """
    cctv: bool
    """
    Indicates if there are CCTV (i.e. closed circuit television) cameras at the stop
    """

@dataclass
class V3StopStaffing:
    """
    
    """
    fri_am_from: str
    """
    Stop staffing hours
    """
    fri_am_to: str
    """
    Stop staffing hours
    """
    fri_pm_from: str
    """
    Stop staffing hours
    """
    fri_pm_to: str
    """
    Stop staffing hours
    """
    mon_am_from: str
    """
    Stop staffing hours
    """
    mon_am_to: str
    """
    Stop staffing hours
    """
    mon_pm_from: str
    """
    Stop staffing hours
    """
    mon_pm_to: str
    """
    Stop staffing hours
    """
    ph_additional_text: str
    """
    Stop staffing hours
    """
    ph_from: str
    """
    Stop staffing hours
    """
    ph_to: str
    """
    Stop staffing hours
    """
    sat_am_from: str
    """
    Stop staffing hours
    """
    sat_am_to: str
    """
    Stop staffing hours
    """
    sat_pm_from: str
    """
    Stop staffing hours
    """
    sat_pm_to: str
    """
    Stop staffing hours
    """
    sun_am_from: str
    """
    Stop staffing hours
    """
    sun_am_to: str
    """
    Stop staffing hours
    """
    sun_pm_from: str
    """
    Stop staffing hours
    """
    sun_pm_to: str
    """
    Stop staffing hours
    """
    thu_am_from: str
    """
    Stop staffing hours
    """
    thu_am_to: str
    """
    Stop staffing hours
    """
    thu_pm_from: str
    """
    Stop staffing hours
    """
    thu_pm_to: str
    """
    Stop staffing hours
    """
    tue_am_from: str
    """
    Stop staffing hours
    """
    tue_am_to: str
    """
    Stop staffing hours
    """
    tue_pm_from: str
    """
    Stop staffing hours
    """
    tue_pm_to: str
    """
    Stop staffing hours
    """
    wed_am_from: str
    """
    Stop staffing hours
    """
    wed_am_to: str
    """
    Stop staffing hours
    """
    wed_pm_from: str
    """
    Stop staffing hours
    """
    wed_pm_To: str
    """
    Stop staffing hours
    """

@dataclass
class V3StopGps:
    """
    
    """
    latitude: float
    """
    Geographic coordinate of latitude at stop
    """
    longitude: float
    """
    Geographic coordinate of longitude at stop
    """

@dataclass
class V3StopAccessibilityWheelchair:
    """
    
    """
    accessible_ramp: bool
    """
    
    """
    parking: bool
    """
    Indicates if there is at least one accessible parking spot at the stop that complies with the Disability Standards for Accessible Public Transport under the Disability Discrimination Act (1992)
    """
    telephone: bool
    """
    Indicates if there is at least one accessible telephone at the stop/platform that complies with the Disability Standards for Accessible Public Transport under the Disability Discrimination Act (1992)
    """
    toilet: bool
    """
    Indicates if there is at least one accessible toilet at the stop/platform that complies with the Disability Standards for Accessible Public Transport under the Disability Discrimination Act (1992)
    """
    low_ticket_counter: bool
    """
    Indicates if there is at least one low ticket counter at the stop that complies with the Disability Standards for Accessible Public Transport under the Disability Discrimination Act (1992)
    """
    manouvering: bool
    """
    Indicates if there is a space for mobility device to board on or off a transport mode
    """
    raised_platform: bool
    """
    Indicates if there is a raised platform to board a train
    """
    ramp: bool
    """
    Indicates if there are ramps (&lt;1:14) at the stop/platform
    """
    secondary_path: bool
    """
    Indicates if there is a path beyond the stop which is accessible
    """
    raised_platform_shelther: bool
    """
    Indicates if there is shelter near the raised platform
    """
    steep_ramp: bool
    """
    Indicates if there are ramps (&gt;1:14) at the stop/platform
    """

@dataclass
class V3StopGeosearch:
    """
    
    """
    disruption_ids: list[int]
    """
    Disruption information identifier(s)
    """
    stop_distance: float
    """
    Distance of stop from input location (in metres); returns 0 if no location is input
    """
    stop_suburb: str
    """
    suburb of stop
    """
    stop_name: str
    """
    Name of stop
    """
    stop_id: int
    """
    Stop identifier
    """
    route_type: int
    """
    Transport mode identifier
    """
    routes: list[object]
    """
    List of routes travelling through the stop
    """
    stop_latitude: float
    """
    Geographic coordinate of latitude at stop
    """
    stop_longitude: float
    """
    Geographic coordinate of longitude at stop
    """
    stop_landmark: str
    """
    Landmark in proximity of stop
    """
    stop_sequence: int
    """
    Sequence of the stop on the route/run; return 0 when route_id or run_id not specified. Order ascendingly by this field (when non zero) to get physical order (earliest first) of stops on the route_id/run_id.
    """

@dataclass
class V3ErrorResponse:
    """
    An error response
    """
    message: str
    """
    Error message
    """
    status: V3Status
    """
    API Status / Metadata
    """

@dataclass
class V3PatternDeparture:
    """
    
    """
    skipped_stops: V3StopModel
    """
    The stops to be skipped following the current departure in order.
    """
    stop_id: int
    """
    Stop identifier
    """
    route_id: int
    """
    Route identifier
    """
    run_id: int
    """
    Numeric trip/service run identifier. Defaults to -1 when run identifier is Alphanumeric
    """
    run_ref: str
    """
    Alphanumeric trip/service run identifier
    """
    direction_id: int
    """
    Direction of travel identifier
    """
    disruption_ids: list[int]
    """
    Disruption information identifier(s)
    """
    scheduled_departure_utc: str
    """
    Scheduled (i.e. timetabled) departure time and date in ISO 8601 UTC format
    """
    estimated_departure_utc: str
    """
    Real-time estimate of departure time and date in ISO 8601 UTC format
    """
    at_platform: bool
    """
    Indicates if the metropolitan train service is at the platform at the time of query; returns false for other modes
    """
    platform_number: str
    """
    Platform number at stop (metropolitan train only; returns null for other modes)
    """
    flags: str
    """
    Flag indicating special condition for run (e.g. RR Reservations Required, GC Guaranteed Connection, DOO Drop Off Only, PUO Pick Up Only, MO Mondays only, TU Tuesdays only, WE Wednesdays only, TH Thursdays only, FR Fridays only, SS School days only; ignore E flag)
    """
    departure_sequence: int
    """
    Chronological sequence for the departures in a run. Order ascendingly by this field to get chronological order (earliest first) of departures with the same run_ref. NOTE, this field is not always N+1 or N-1 of the previous or following departure. e.g 100, 200, 250, 300 instead of 1, 2, 3, 4
    """

@dataclass
class V3StoppingPatternStop:
    """
    
    """
    stop_ticket: V3StopTicket
    """
    Stop ticket information
    """
    stop_distance: float
    """
    Distance of stop from input location (in metres); returns 0 if no location is input
    """
    stop_suburb: str
    """
    suburb of stop
    """
    stop_name: str
    """
    Name of stop
    """
    stop_id: int
    """
    Stop identifier
    """
    route_type: int
    """
    Transport mode identifier
    """
    stop_latitude: float
    """
    Geographic coordinate of latitude at stop
    """
    stop_longitude: float
    """
    Geographic coordinate of longitude at stop
    """
    stop_landmark: str
    """
    Landmark in proximity of stop
    """
    stop_sequence: int
    """
    Sequence of the stop on the route/run; return 0 when route_id or run_id not specified. Order ascendingly by this field (when non zero) to get physical order (earliest first) of stops on the route_id/run_id.
    """

@dataclass
class V3ResultRoute:
    """
    
    """
    route_name: str
    """
    Name of route
    """
    route_number: str
    """
    Route number presented to public (nb. not route_id)
    """
    route_type: int
    """
    Transport mode identifier
    """
    route_id: int
    """
    Route identifier
    """
    route_gtfs_id: str
    """
    GTFS Identifer of the route
    """
    route_service_status: V3RouteServiceStatus
    """
    Service status for the route (indicates disruptions)
    """

@dataclass
class V3GenerateDivaMappingResponse:
    """
    
    """
    mapping_version: str
    """
    
    """
    status: V3Status
    """
    API Status / Metadata
    """

@dataclass
class V3SiriEstimatedTimetableSubscriptionRequest:
    """
    
    """
    preview_interval: str
    """
    Siri Preview Interval
    """
    subscriber_ref: str
    """
    Siri Subscriber Ref
    """
    subscription_ref: str
    """
    Siri Subscription Ref - Unique to a Subscriber Ref
    """
    siri_format: int
    """
    Siri Message Format 'xml' or 'json'
    """
    siri_version: str
    """
    Siri Message Version '1.3' or '2.0'
    """
    consumer_address: str
    """
    Siri Consumer Address - Baseline and Updates will be sent to this address
    """
    initial_termination_time: str
    """
    Siri Initial Termination Time - Expiry of the subscription
    """
    topics: V3SiriSubscriptionTopic
    """
    
    """

@dataclass
class V3StopOnRoute:
    """
    
    """
    disruption_ids: list[int]
    """
    Disruption information identifier(s)
    """
    stop_suburb: str
    """
    suburb of stop
    """
    route_type: int
    """
    Transport mode identifier
    """
    stop_latitude: float
    """
    Geographic coordinate of latitude at stop
    """
    stop_longitude: float
    """
    Geographic coordinate of longitude at stop
    """
    stop_sequence: int
    """
    Sequence of the stop on the route/run; return 0 when route_id or run_id not specified. Order ascendingly by this field (when non zero) to get physical order (earliest first) of stops on the route_id/run_id.
    """
    stop_ticket: V3StopTicket
    """
    Stop ticket information
    """
    stop_id: int
    """
    Stop identifier
    """
    stop_name: str
    """
    Name of stop
    """
    stop_landmark: str
    """
    Landmark in proximity of stop
    """

@dataclass
class V3Run:
    """
    
    """
    run_id: int
    """
    Numeric trip/service run identifier. Defaults to -1 when run identifier is Alphanumeric
    """
    run_ref: str
    """
    Alphanumeric trip/service run identifier
    """
    route_id: int
    """
    Route identifier
    """
    route_type: int
    """
    Transport mode identifier
    """
    final_stop_id: int
    """
    stop_id of final stop of run
    """
    destination_name: str
    """
    Name of destination of run
    """
    status: str
    """
    Status of metropolitan train run; returns "scheduled" for other modes
    """
    direction_id: int
    """
    Direction of travel identifier
    """
    run_sequence: int
    """
    Chronological sequence of the trip/service run on the route in direction. Order ascendingly by this field to get chronological order (earliest first) of runs with the same route_id and direction_id.
    """
    express_stop_count: int
    """
    The number of remaining skipped/express stations for the run/service from a stop
    """
    vehicle_position: V3VehiclePosition
    """
    Position of the trip/service run. Available for some Bus, Nightrider and Train runs. May be null.
    """
    vehicle_descriptor: V3VehicleDescriptor
    """
    Descriptor of the trip/service run. Only available for some runs. May be null.
    """
    geopath: list[object]
    """
    Geopath of the route
    """

@dataclass
class V3DisruptionRoute:
    """
    
    """
    route_type: int
    """
    Transport mode identifier
    """
    route_id: int
    """
    Route identifier
    """
    route_name: str
    """
    Name of route
    """
    route_number: str
    """
    Route number presented to public (i.e. not route_id)
    """
    route_gtfs_id: str
    """
    GTFS Identifer of the route
    """
    direction: V3DisruptionDirection
    """
    Direction of travel relevant to a disruption (if applicable)
    """

@dataclass
class V3StopDepartureRequest:
    """
    
    """
    route_type: int
    """
    Number identifying transport mode; values returned via RouteTypes API
    """
    stop_id: int
    """
    Identifier of stop; values returned by Stops API
    """
    max_results: int
    """
    Maximum number of results returned
    """
    gtfs: bool
    """
    Indicates that stop_id parameter will accept "GTFS stop_id" data and route_directions[x].route_id parameters will accept route_gtfs_id data
    """
    route_directions: V3StopDepartureRequestRouteDirection
    """
    The route directions to find departures for at this stop.
    """

@dataclass
class V3BulkDeparturesUpdateResponse:
    """
    
    """
    departures: V3Departure
    """
    Timetabled and real-time service departures
    """
    route_type: int
    """
    Transport mode identifier
    """
    stop_id: int
    """
    Stop identifier
    """
    requested_route_direction: V3BulkDeparturesRouteDirectionResponse
    """
    The route direction that these departures are for. Will be one of the requested route directions
    """
    route_direction_status: int
    """
    The status of the route direction (changed | unchanged).
    If changed, requests should change the requested_route_direction for the route_direction supplied.
    """
    route_direction: V3BulkDeparturesRouteDirectionResponse
    """
    The route direction found matching the requested_route_direction
    """

@dataclass
class V3DirectionsResponse:
    """
    
    """
    directions: V3DirectionWithDescription
    """
    Directions of travel of route
    """
    status: V3Status
    """
    API Status / Metadata
    """

@dataclass
class V3DisruptionModesResponse:
    """
    
    """
    disruption_modes: V3DisruptionMode
    """
    Transport mode identifiers
    """
    status: V3Status
    """
    API Status / Metadata
    """

@dataclass
class V3OutletResponse:
    """
    
    """
    outlets: V3Outlet
    """
    myki ticket outlets
    """
    status: V3Status
    """
    API Status / Metadata
    """

@dataclass
class V3OutletGeolocationResponse:
    """
    
    """
    outlets: V3OutletGeolocation
    """
    myki ticket outlets
    """
    status: V3Status
    """
    API Status / Metadata
    """

@dataclass
class V3RouteWithStatus:
    """
    
    """
    route_service_status: V3RouteServiceStatus
    """
    Service status for the route (indicates disruptions)
    """
    route_type: int
    """
    Transport mode identifier
    """
    route_id: int
    """
    Route identifier
    """
    route_name: str
    """
    Name of route
    """
    route_number: str
    """
    Route number presented to public (nb. not route_id)
    """
    route_gtfs_id: str
    """
    GTFS Identifer of the route
    """
    geopath: list[object]
    """
    GeoPath of the route
    """

@dataclass
class V3RouteTypesResponse:
    """
    
    """
    route_types: V3RouteType
    """
    Transport mode identifiers
    """
    status: V3Status
    """
    API Status / Metadata
    """

@dataclass
class V3SiriReferenceDataRequest:
    """
    
    """
    line_refs: V3SiriLineRefDirectionRefStopPointRef
    """
    
    """
    stop_point_refs: list[int]
    """
    Siri StopPointRef
    """
    date_utc: str
    """
    Filter by the date and time of the request (ISO 8601 UTC format) (default = current date and time)
    """
    mapping_version: str
    """
    DIVA mapping version generated by Chronos during a Parser or RealtimeBusConfig load
    """

@dataclass
class V3SiriStopsRefsDictionary:
    """
    
    """
    stop_point_refs: V3SiriReferenceDataDetail
    """
    
    """
    unmatched_stop_point_refs: str
    """
    
    """

@dataclass
class V3SiriLineRefsRequest:
    """
    
    """
    line_refs: V3SiriLineRef
    """
    
    """
    mapping_version: str
    """
    DIVA mapping version generated by Chronos during a Parser or RealtimeBusConfig load
    """

@dataclass
class V3SiriLineRefMappingsResponse:
    """
    
    """
    mapping_version: str
    """
    
    """
    line_refs: V3SiriLineRefDirectionRefsDictionary
    """
    
    """
    status: V3Status
    """
    API Status / Metadata
    """

@dataclass
class V3DynamoDbTimetablesReponse:
    """
    
    """
    timetables: V3DynamoDbTimetable
    """
    
    """
    status: V3Status
    """
    API Status / Metadata
    """

@dataclass
class V3SiriDownstreamSubscription:
    """
    
    """
    subscriber_ref: str
    """
    
    """
    subscription_ref: str
    """
    
    """
    message_type: int
    """
    
    """
    siri_format: int
    """
    
    """
    siri_version: str
    """
    
    """
    consumer_address: str
    """
    
    """
    initial_termination_time: str
    """
    
    """
    validity_period_start: str
    """
    
    """
    validity_period_end: str
    """
    
    """
    preview_interval: str
    """
    
    """
    topics: V3SiriDownstreamSubscriptionTopic
    """
    
    """

@dataclass
class V3SiriProductionTimetableSubscriptionRequest:
    """
    
    """
    start_time: str
    """
    Siri Start Time of the Validity Period
    """
    end_time: str
    """
    Siri End Time of the Validity Period
    """
    subscriber_ref: str
    """
    Siri Subscriber Ref
    """
    subscription_ref: str
    """
    Siri Subscription Ref - Unique to a Subscriber Ref
    """
    siri_format: int
    """
    Siri Message Format 'xml' or 'json'
    """
    siri_version: str
    """
    Siri Message Version '1.3' or '2.0'
    """
    consumer_address: str
    """
    Siri Consumer Address - Baseline and Updates will be sent to this address
    """
    initial_termination_time: str
    """
    Siri Initial Termination Time - Expiry of the subscription
    """
    topics: V3SiriSubscriptionTopic
    """
    
    """

@dataclass
class V3StopLocation:
    """
    
    """
    gps: V3StopGps
    """
    GPS coordinates of the stop
    """

@dataclass
class V3StopAccessibility:
    """
    
    """
    lighting: bool
    """
    Indicates if there is lighting at the stop
    """
    platform_number: int
    """
    Indicates the platform number for xivic information (Platform 0 indicates general stop facilities)
    """
    audio_customer_information: bool
    """
    Indicates if there is at least one audio customer information at the stop/platform
    """
    escalator: bool
    """
    Indicates if there is at least one accessible escalator at the stop/platform that complies with the Disability Standards for Accessible Public Transport under the Disability Discrimination Act (1992)
    """
    hearing_loop: bool
    """
    Indicates if there is a hearing loop facility at the stop/platform
    """
    lift: bool
    """
    Indicates if there is an elevator at the stop/platform
    """
    stairs: bool
    """
    Indicates if there are stairs available in the stop
    """
    stop_accessible: bool
    """
    Indicates if the stop is accessible
    """
    tactile_ground_surface_indicator: bool
    """
    Indicates if there are tactile tiles (also known as tactile ground surface indicators, or TGSIs) at the stop
    """
    waiting_room: bool
    """
    Indicates if there is a general waiting area at the stop
    """
    wheelchair: V3StopAccessibilityWheelchair
    """
    Facilities relating to the accessibility of the stop by wheelchair
    """

@dataclass
class V3RunsResponse:
    """
    
    """
    runs: V3Run
    """
    Individual trips/services of a route
    """
    status: V3Status
    """
    API Status / Metadata
    """

@dataclass
class V3RunResponse:
    """
    
    """
    run: V3Run
    """
    Individual trip/service of a route
    """
    status: V3Status
    """
    API Status / Metadata
    """

@dataclass
class V3ResultStop:
    """
    
    """
    stop_distance: float
    """
    Distance of stop from input location (in metres); returns 0 if no location is input
    """
    stop_suburb: str
    """
    suburb of stop
    """
    route_type: int
    """
    Transport mode identifier
    """
    routes: V3ResultRoute
    """
    List of routes travelling through the stop
    """
    stop_latitude: float
    """
    Geographic coordinate of latitude at stop
    """
    stop_longitude: float
    """
    Geographic coordinate of longitude at stop
    """
    stop_sequence: int
    """
    Sequence of the stop on the route/run; return 0 when route_id or run_id not specified. Order ascendingly by this field (when non zero) to get physical order (earliest first) of stops on the route_id/run_id.
    """
    stop_id: int
    """
    Stop identifier
    """
    stop_name: str
    """
    Name of stop
    """
    stop_landmark: str
    """
    Landmark in proximity of stop
    """

@dataclass
class V3Disruption:
    """
    
    """
    disruption_id: int
    """
    Disruption information identifier
    """
    title: str
    """
    Headline title summarising disruption information
    """
    url: str
    """
    URL of relevant article on PTV website
    """
    description: str
    """
    Description of the disruption
    """
    disruption_status: str
    """
    Status of the disruption (e.g. "Planned", "Current")
    """
    disruption_type: str
    """
    Type of disruption
    """
    published_on: str
    """
    Date and time disruption information is published on PTV website, in ISO 8601 UTC format
    """
    last_updated: str
    """
    Date and time disruption information was last updated by PTV, in ISO 8601 UTC format
    """
    from_date: str
    """
    Date and time at which disruption begins, in ISO 8601 UTC format
    """
    to_date: str
    """
    Date and time at which disruption ends, in ISO 8601 UTC format (returns null if unknown)
    """
    routes: V3DisruptionRoute
    """
    Route relevant to a disruption (if applicable)
    """
    stops: V3DisruptionStop
    """
    Stop relevant to a disruption (if applicable)
    """
    colour: str
    """
    
    """
    display_on_board: bool
    """
    
    """
    display_status: bool
    """
    
    """

@dataclass
class V3BulkDeparturesRequest:
    """
    
    """
    requests: V3StopDepartureRequest
    """
    Collection of departure requests
    """
    date_utc: str
    """
    Filter by the date and time of the request (ISO 8601 UTC format) (default = current date and time)
    """
    look_backwards: bool
    """
    Indicates if filtering runs (and their departures) to those that arrive at destination before date_utc (default = false). Requires max_results &gt; 0.
    """
    include_cancelled: bool
    """
    Indicates if cancelled services (if they exist) are returned (default = false) - metropolitan train only
    """
    include_geopath: bool
    """
    Indicates if the route geopath should be returned
    """
    expand: list[str]
    """
    List objects to be returned in full (i.e. expanded) - options include: all, stop, route, run, direction, disruption, none
    """

@dataclass
class V3RouteResponse:
    """
    
    """
    route: V3RouteWithStatus
    """
    Train lines, tram routes, bus routes, regional coach routes, Night Bus routes
    """
    status: V3Status
    """
    API Status / Metadata
    """

@dataclass
class V3SiriDirectionRefsDictionary:
    """
    
    """
    direction_refs: V3SiriStopsRefsDictionary
    """
    
    """

@dataclass
class V3StopDetails:
    """
    
    """
    disruption_ids: list[int]
    """
    Disruption information identifier(s)
    """
    station_type: str
    """
    Type of metropolitan train station (i.e. "Premium", "Host" or "Unstaffed" station); returns null for V/Line train
    """
    station_description: str
    """
    The definition applicable to the station_type; returns null for V/Line train
    """
    route_type: int
    """
    Transport mode identifier
    """
    stop_location: V3StopLocation
    """
    Location details of the stop
    """
    stop_amenities: V3StopAmenityDetails
    """
    Amenity and facility details at the stop
    """
    stop_accessibility: V3StopAccessibility
    """
    Facilities relating to the accessibility of the stop
    """
    stop_staffing: V3StopStaffing
    """
    Staffing details for the stop
    """
    routes: list[object]
    """
    Routes travelling through the stop
    """
    stop_id: int
    """
    Stop identifier
    """
    stop_name: str
    """
    Name of stop
    """
    stop_landmark: str
    """
    Landmark in proximity of stop
    """

@dataclass
class V3BulkDeparturesResponse:
    """
    
    """
    responses: V3BulkDeparturesUpdateResponse
    """
    Contains departures for the requested stop and route(s). It includes details as to the route_direction and whether it is still valid.
    """
    stops: V3BulkDeparturesStopResponse
    """
    A train station, tram stop, bus stop, regional coach stop or Night Bus stop
    """
    routes: list[object]
    """
    Train lines, tram routes, bus routes, regional coach routes, Night Bus routes
    """
    runs: V3Run
    """
    Individual trips/services of a route
    """
    directions: V3Direction
    """
    Directions of travel of route
    """
    disruptions: V3Disruption
    """
    Disruption information applicable to relevant routes or stops
    """
    status: V3Status
    """
    API Status / Metadata
    """

@dataclass
class V3Disruptions:
    """
    
    """
    general: V3Disruption
    """
    Subset of disruption information applicable to multiple route_types
    """
    metro_train: V3Disruption
    """
    Subset of disruption information applicable to metropolitan train
    """
    metro_tram: V3Disruption
    """
    Subset of disruption information applicable to metropolitan tram
    """
    metro_bus: V3Disruption
    """
    Subset of disruption information applicable to metropolitan bus
    """
    regional_train: V3Disruption
    """
    Subset of disruption information applicable to V/Line train
    """
    regional_coach: V3Disruption
    """
    Subset of disruption information applicable to V/Line coach
    """
    regional_bus: V3Disruption
    """
    Subset of disruption information applicable to regional bus
    """
    school_bus: V3Disruption
    """
    Subset of disruption information applicable to school bus
    """
    telebus: V3Disruption
    """
    Subset of disruption information applicable to telebus services
    """
    night_bus: V3Disruption
    """
    Subset of disruption information applicable to night bus
    """
    ferry: V3Disruption
    """
    Subset of disruption information applicable to ferry
    """
    interstate_train: V3Disruption
    """
    Subset of disruption information applicable to interstate train
    """
    skybus: V3Disruption
    """
    Subset of disruption information applicable to skybus
    """
    taxi: V3Disruption
    """
    Subset of disruption information applicable to taxi
    """

@dataclass
class V3DisruptionResponse:
    """
    
    """
    disruption: V3Disruption
    """
    Disruption information applicable to relevant routes or stops
    """
    status: V3Status
    """
    API Status / Metadata
    """

@dataclass
class V3StoppingPattern:
    """
    
    """
    disruptions: V3Disruption
    """
    Disruption information applicable to relevant routes or stops
    """
    departures: V3PatternDeparture
    """
    Timetabled and real-time service departures
    """
    stops: V3StoppingPatternStop
    """
    A train station, tram stop, bus stop, regional coach stop or Night Bus stop
    """
    routes: object
    """
    Train lines, tram routes, bus routes, regional coach routes, Night Bus routes
    """
    runs: V3Run
    """
    Individual trips/services of a route
    """
    directions: V3Direction
    """
    Directions of travel of route
    """
    status: V3Status
    """
    API Status / Metadata
    """

@dataclass
class V3SearchResult:
    """
    
    """
    stops: V3ResultStop
    """
    Train stations, tram stops, bus stops, regional coach stops or Night Bus stops
    """
    routes: V3ResultRoute
    """
    Train lines, tram routes, bus routes, regional coach routes, Night Bus routes
    """
    outlets: V3ResultOutlet
    """
    myki ticket outlets
    """
    status: V3Status
    """
    API Status / Metadata
    """

@dataclass
class V3StopsOnRouteResponse:
    """
    
    """
    stops: V3StopOnRoute
    """
    Train stations, tram stops, bus stops, regional coach stops or Night Bus stops
    """
    disruptions: V3Disruption
    """
    Disruption information applicable to relevant routes or stops
    """
    geopath: list[object]
    """
    GeoPath for the route
    """
    status: V3Status
    """
    API Status / Metadata
    """

@dataclass
class V3StopsByDistanceResponse:
    """
    
    """
    stops: V3StopGeosearch
    """
    Train stations, tram stops, bus stops, regional coach stops or Night Bus stops
    """
    disruptions: V3Disruption
    """
    Disruption information applicable to relevant routes or stops
    """
    status: V3Status
    """
    API Status / Metadata
    """

@dataclass
class V3DeparturesResponse:
    """
    
    """
    departures: V3Departure
    """
    Timetabled and real-time service departures
    """
    stops: V3StopModel
    """
    A train station, tram stop, bus stop, regional coach stop or Night Bus stop
    """
    routes: object
    """
    Train lines, tram routes, bus routes, regional coach routes, Night Bus routes
    """
    runs: V3Run
    """
    Individual trips/services of a route
    """
    directions: V3Direction
    """
    Directions of travel of route
    """
    disruptions: V3Disruption
    """
    Disruption information applicable to relevant routes or stops
    """
    status: V3Status
    """
    API Status / Metadata
    """

@dataclass
class V3SiriReferenceDataMappingsResponse:
    """
    
    """
    mapping_version: str
    """
    
    """
    line_refs: V3SiriDirectionRefsDictionary
    """
    SIRI LineRef
    """
    stop_point_refs: V3StopPoint
    """
    
    """
    status: V3Status
    """
    API Status / Metadata
    """

@dataclass
class V3StopResponse:
    """
    
    """
    stop: V3StopDetails
    """
    A metropolitan or V/Line train station
    """
    disruptions: V3Disruption
    """
    Disruption information applicable to relevant routes or stops
    """
    status: V3Status
    """
    API Status / Metadata
    """

@dataclass
class V3DisruptionsResponse:
    """
    
    """
    disruptions: V3Disruptions
    """
    Disruption information applicable to relevant routes or stops
    """
    status: V3Status
    """
    API Status / Metadata
    """

