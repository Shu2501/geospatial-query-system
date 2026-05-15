from flask import Flask, render_template, request

from modules.nlp_processor import extract_query_data
from modules.geolocator import get_coordinates
from modules.query_engine import (
    search_places,
    search_places_nearby
)
from modules.map_generator import generate_map

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    coordinates = None
    places = []
    image_name = "default"

    if request.method == "POST":

        user_query = request.form["query"]

        # GPS coordinates from browser
        latitude = request.form.get("latitude")
        longitude = request.form.get("longitude")

        # NLP extraction
        result = extract_query_data(user_query)

        # ----------------------------------------
        # CURRENT LOCATION SEARCH
        # ----------------------------------------

        if (
            result["location"] == "CURRENT_LOCATION"
            and latitude
            and longitude
        ):

            coordinates = {

                "latitude": latitude,
                "longitude": longitude

            }

            places = search_places_nearby(

                latitude,

                longitude,

                result["place_type"]
            )

        # ----------------------------------------
        # NORMAL CITY SEARCH
        # ----------------------------------------

        elif result["location"]:

            coordinates = get_coordinates(

                result["location"]
            )

            if coordinates and result["place_type"]:

                places = search_places(

                    result["location"],

                    result["place_type"]

                )

        # ----------------------------------------
        # IMAGE NAME
        # ----------------------------------------

        if result and result["place_type"]:
            image_name = result["place_type"].replace(" ", "_") + ".png"
        else:
            image_name = "default.png"

        print(places)

    # ----------------------------------------
    # GENERATE MAP
    # ----------------------------------------

    error_message = None

    if request.method == "POST" and not places:

        error_message = "No places found. Please try a different query."

    if places:

        generate_map(places)

    return render_template(

        "index.html",

        result=result,

        coordinates=coordinates,

        places=places,

        image_name=image_name,

        error_message=error_message
    )

if __name__ == "__main__":

    app.run(debug=True)