import math


class GeographicalLocation(object):

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def distance_to(self, GeographicalLocation):
        R = 6371
        lat_distance = math.radians(GeographicalLocation.latitude
                                    - self.latitude)
        lon_distance = math.radians(GeographicalLocation.longitude
                                    - self.longitude)
        a = math.sin(lat_distance / 2) * math.sin(lat_distance / 2)\
            + math.cos(math.radians(self.latitude)) * \
            math.cos(math.radians(GeographicalLocation.latitude))\
            * math.sin(lon_distance / 2) \
            * math.sin(lon_distance / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c * 1000
        return distance
