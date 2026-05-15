from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geo_project")

SEARCH_MAPPINGS = {

    "train station": "railway station",
    "bus station": "bus stop",
    "movie theater": "cinema",
    "tourist place": "tourist attraction"

}

def search_places(location, place_type):

    # Smart keyword mapping
    if place_type in SEARCH_MAPPINGS:

        place_type = SEARCH_MAPPINGS[place_type]

    if place_type == "tourist attraction":

        query = f"famouse places near {location}, India"

    else:

        query = f"{place_type} near {location}, India"

    try:

        places = geolocator.geocode(

            query,

            exactly_one=False,

            limit=10

        )

        results = []

        if places:

            for place in places:

                results.append({

                    "name": place.address.split(",")[0],

                    "full_address": place.address,

                    "latitude": place.latitude,

                    "longitude": place.longitude

                })

        return results

    except Exception as e:

        print("ERROR:", e)

        return []


# ----------------------------------------
# CURRENT LOCATION SEARCH
# ----------------------------------------

def search_places_nearby(latitude, longitude, place_type):

    try:

        # Reverse geocoding
        location = geolocator.reverse(

            f"{latitude}, {longitude}",

            exactly_one=True
        )

        address = location.raw.get("address", {})

        city = (

            address.get("city")

            or address.get("town")

            or address.get("state_district")

            or address.get("state")

        )

        print("DETECTED CITY:", city)

        # Reuse existing search
        return search_places(

            city,

            place_type
        )

    except Exception as e:

        print("ERROR:", e)

        return []