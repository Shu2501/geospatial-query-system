import folium


def generate_map(places):

    # Default center
    start_coords = [20.5937, 78.9629]

    # If places exist, center map on first place
    if places:

        start_coords = [

            places[0]["latitude"],

            places[0]["longitude"]

        ]

    # Create map
    geo_map = folium.Map(

        location=start_coords,

        zoom_start=13

    )

    # Add markers
    for place in places:

        folium.Marker(

            [

                place["latitude"],

                place["longitude"]

            ],

            popup=place["name"],

            tooltip=place["name"]

        ).add_to(geo_map)

    # Save map
    geo_map.save(

        "static/maps/map.html"
    )