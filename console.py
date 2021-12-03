import pdb
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

country_repository.delete_all()
city_repository.delete_all()

country_1 = Country("Latvia", "Riga", 1857200, True)
country_repository.save(country_1)
country_2 = Country("Australia", "Canberra", 25929200)
country_repository.save(country_2)

city_1 = City("Perth", country_2, "Kings park segway tours, Street art and sculpture tour, Perth video game console museum")
city_repository.save(city_1)
city_2 = City("Jelgava", country_1, "Jalgava Palace, Eleja manor park and Tea house, Zemgales Olympic centre", True)
city_repository.save(city_2)

cities = city_repository.select_all()
print(cities)

cities_for_australia = city_repository.select_all_from_country(country_2.id)
for city in cities_for_australia:
    print(city.__dict__)

pdb.set_trace()