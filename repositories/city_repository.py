from db.run_sql import run_sql
from models.city import City
import repositories.country_repository as country_repository


def save(city):
    sql = "INSERT INTO cities (name, country_id, places_of_interest, visited) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [city.name, city.country.id, city.places_of_interest, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id 
    return city 

def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['places_of_interest'], row['visited'], row['id'])
        cities.append(city)
    return cities

def select_all_from_country(country_id):
    cities=[]

    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [country_id]
    results = run_sql(sql, values)

    for row in results:
        country = country_repository.select(country_id)
        city = City(row['name'], country, row['places_of_interest'], row['visited'], row['id'])
        cities.append(city)
    return cities

def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = country_repository.select(result['country_id'])
        city = City(result['name'], country, result['places_of_interest'], result['visited'], result['id'])
    return city

def delete_all():
    sql = "DELETE  FROM cities"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(city):
    sql = "UPDATE cities SET (name, country_id, places_of_interest, visited) = (%s, %s, %s, %s) WHERE id = %s"
    values = [city.name, city.country.id, city.places_of_interest, city.visited, city.id]
    run_sql(sql, values)