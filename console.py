import pdb
from models.city import City
from models.country import Country
from models.poi import PlaceOfInterest

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.poi_repository as poi_repository

country_repository.delete_all()
city_repository.delete_all()
poi_repository.delete_all()

country_1 = Country("Latvia", "Riga", True)
country_repository.save(country_1)
country_2 = Country("Australia", "Canberra")
country_repository.save(country_2)
country_3 = Country("Scotland", "Edinburgh", True)
country_repository.save(country_3)
country_4 = Country("Venezuela", "Caracus")
country_repository.save(country_4)
country_5 = Country("Iceland", "Reykjavík", True)

city_1 = City("Perth", country_2)
city_repository.save(city_1)
city_2 = City("Jelgava", country_1, True)
city_repository.save(city_2)
city_3 = City("Riga", country_1, True)
city_repository.save(city_3)
city_4 = City("Dundee", country_3, True)
city_repository.save(city_4)
city_5 = City("Glasgow", country_3)
city_repository.save(city_5)

poi_1 = PlaceOfInterest("Perth video game console museum", "Explore the museum that houses more than 100 consoles from the 1970s through to the 2000s", city_1)
poi_repository.save(poi_1)
poi_2 = PlaceOfInterest("Central Market", "Buy food, trinkets, clothes and other things!", True)
poi_repository.save(poi_2)

cities = city_repository.select_all()
print(cities)

cities_for_australia = city_repository.select_all_from_country(country_2.id)
for city in cities_for_australia:
    print(city.__dict__)

poi_for_perth = poi_repository.select_all_from_city(city_1.id)
for poi_repository in poi_for_perth:
    print(poi_repository.__dict__)

pdb.set_trace()