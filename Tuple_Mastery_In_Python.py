# Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. 
# Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
# The function should format and return a string that lists each itinerary. 
# For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, 
# the output should be a string formatted as:

# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"

itineraries = [
    ("Alice", "New York", "Mexico" ),
    ("Sam", "Texas", "Illinois" ),
    ("Savana", "Ohio", "Wisconsin")

]

def list_itineraries(itineraries):
    itinerary_str = "" # Initializes an empty string
    for itinerary in itineraries:
        traveler_name, origin, destination = itinerary # Helps unpack the itinerary tuple
        itinerary_str += f"{traveler_name} - From {origin} to {destination}.\n" # Will grab the unpacked values and start a new line after each iteration
    return itinerary_str

print(list_itineraries(itineraries))