from math import radians, cos, sin, asin, sqrt

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r




def assignCrimesToStops(crimes, stops):
    stops_lookup = initializeStops(stops)
    
    for crime in crimes:
        stop_id = -1
        max_distance = foat("inf")
        for stop in stops:
            dist = haversine(crime.lat, crime.long, stop.lat, stop.long)
            if dist < max_distance:
                max_distance = dist
                stop_id = stop.id

        stops_lookup[stop_id].append(crime)

    return stops_lookup


def initializeStops(stops):
    stops_lookup = {}
    for stop in stops:
        stops_lookup[stop.id] = []
