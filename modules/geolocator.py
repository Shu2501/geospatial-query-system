from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geo_project")

def get_coordinates(location_name):

    location_name = " ".join(location_name.split())

    location = geolocator.geocode(location_name)

    if location:

        return {
            "latitude": location.latitude,
            "longitude": location.longitude
        }

    return None
