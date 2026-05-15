import spacy

nlp = spacy.load("en_core_web_sm")

PLACE_TYPES = {

    "hospital": "hospital",

    "school": "school",
    "schools": "school",

    "restaurant": "restaurant",
    "restaurants": "restaurant",

    "mall": "mall",

    "cafe": "cafe",
    "cafes": "cafe",

    "bank": "bank",

    "pharmacy": "pharmacy",

    "park": "park",
    "parks": "park",

    "library": "library",
    "libraries": "library",

    "college": "college",
    "university": "university",

    "gym": "fitness center",
    "gyms": "fitness center",

    "hotel": "hotel",
    "hotels": "hotel",

    "supermarket": "supermarket",
    "airport": "airport",

    "bus station": "bus stand",
    "bus stations": "bus stand",

    "train station": "railway station",
    "train stations": "railway station",

    "metro station": "metro station",

    "movie theater": "cinema",
    "cinema": "cinema",
    "theater": "cinema",

    "tourist place": "tourist attraction",
    "tourist places": "tourist attraction",

    "clinic": "clinic",
    "clinics": "clinic"
}

def extract_query_data(query):

    doc = nlp(query)

    location = None
    place_type = None

    #Extract locations
    for ent in doc.ents:

        if ent.label_ in ["GPE", "LOC"]:
            location = ent.text

    #Extract place types
    query_lower = query.lower()

    if "nearby" in query_lower:
        location = "CURRENT_LOCATION"

    for place in PLACE_TYPES:

        if place in query_lower:
            place_type = PLACE_TYPES[place]
    
    return {
        "location": location,
        "place_type": place_type
    }