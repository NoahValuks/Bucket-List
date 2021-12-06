class Country:
    def __init__(self, name, capital, visited = False, id = None):
        self.name = name
        self.capital = capital
        self.visited = visited
        self.id = id

    def mark_visited(self):
        self.visited = True