import pdb
from models.city import City
from models.country import Country
from models.place_of_interest import PlaceOfInterest

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.place_of_interest_repository as place_of_interest_repository

country_repository.delete_all()
city_repository.delete_all()
place_of_interest_repository.delete_all()

country_1 = Country("Latvia", "Riga", 1857200, True)
country_repository.save(country_1)
country_2 = Country("Australia", "Canberra", 25929200)
country_repository.save(country_2)

city_1 = City("Perth", country_2)
city_repository.save(city_1)
city_2 = City("Jelgava", country_1, True)
city_repository.save(city_2)

place_of_interest_1 = PlaceOfInterest("Perth video game console museum", "Explore the museum that houses more than 100 consoles from the 1970s through to the 2000s", city_1)
place_of_interest_repository.save(place_of_interest_1)

cities = city_repository.select_all()
print(cities)

cities_for_australia = city_repository.select_all_from_country(country_2.id)
for city in cities_for_australia:
    print(city.__dict__)

poi_for_perth = place_of_interest_repository.select_all_from_city(city_1.id)
for poi in poi_for_perth:
    print(poi.__dict__)

pdb.set_trace()