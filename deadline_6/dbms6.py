from geopy.geocoders import Nominatim
from geopy.distance import great_circle
from geopy.exc import GeocoderTimedOut

def get_coordinates(location_string):
    geolocator = Nominatim(user_agent="geo_distance_calculator")
    try:
        location = geolocator.geocode(location_string)
        if location is not None:
            return location.latitude, location.longitude
        else:
            print(f"Could not find coordinates for {location_string}.")
            return None
    except GeocoderTimedOut:
        print("Geocoder service timed out. Please try again later.")
        return None

def calculate_distance(location1, location2):
    coordinates1 = get_coordinates(location1)
    coordinates2 = get_coordinates(location2)
    
    if coordinates1 is not None and coordinates2 is not None:
        return great_circle(coordinates1, coordinates2).kilometers
    else:
        return None

location1 = "Building B12, New Delhi"
location2 = "New York City, NY, USA"

distance = calculate_distance(location1, location2)
if distance is not None:
    print(f"Distance between {location1} and {location2}: {distance:.2f} km")
else:
    print("Could not calculate distance due to missing coordinates.")
