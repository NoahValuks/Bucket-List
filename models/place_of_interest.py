class PlaceOfInterest:
    def __init__(self, name, information, city, visited=False, id=None):
        self.name = name
        self.information =information
        self.city = city
        self.visited = visited
        self.id = id

    def mark_visited(self):
        self.visited = True
