import googlemaps
from datetime import datetime

# Enter your Google Maps API key here
gmaps = googlemaps.Client(key='YOUR_API_KEY')

# Define the two locations
origin = "New York City, NY"
destination = "Washington D.C."

# Call the distance_matrix function with the origin and destination
distance_result = gmaps.distance_matrix(origin, destination)

# Extract the distance in meters
distance = distance_result['rows'][0]['elements'][0]['distance']['value']

# Convert the distance to miles
distance_miles = distance * 0.000621371

print("The distance between", origin, "and", destination, "is", round(distance_miles,2), "miles.")
