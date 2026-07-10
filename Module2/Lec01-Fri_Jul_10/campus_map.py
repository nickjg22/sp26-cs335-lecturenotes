# campus_map.py

campus_map = {
    "Library": ["Student Center", "Science Building"],
    "Student Center": ["Library", "Gym", "Cafeteria"],
    "Science Building": ["Library", "Engineering Lab"],
    "Gym": ["Student Center"],
    "Cafeteria": ["Student Center"],
    "Engineering Lab": ["Science Building"],
}


def show_neighbors(campus_map, location):
    """
    Print all locations directly connected to the given location.
    """
    # TODO: Check whether location is in campus_map

    # TODO: If not found, print a helpful message

    # TODO: If found, print the location name

    # TODO: Loop through the location's neighbors and print each one
    pass


# Demo calls
show_neighbors(campus_map, "Library")
show_neighbors(campus_map, "Gym")
show_neighbors(campus_map, "Parking Lot")
