class Country:
    def __init__(self, name, capital, population, visited = False, id = None):
        self.name = name
        self.capital = capital
        self.population = population
        self.visited = visited
        self.id = id

    def mark_visited(self):
        self.visited = True