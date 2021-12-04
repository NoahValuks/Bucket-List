class City:
    def __init__(self, name, country, places_of_interest = [], visited = False, id = None):
        self.name = name
        self.country = country
        self.places_of_interest = places_of_interest
        self.visited = visited
        self.id = id

    def mark_visited(self):
        self.visited = True