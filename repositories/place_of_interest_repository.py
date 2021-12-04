from db.run_sql import run_sql
from models.place_of_interest import PlaceOfInterest
import repositories.city_repository as city_repository

def save(place_of_interest):
    sql = "INSERT INTO places_of_interest (name, information, city_id, visited) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [place_of_interest.name, place_of_interest.information, place_of_interest.city.id, place_of_interest.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    place_of_interest.id = id 
    return place_of_interest 

def select_all():
    places_of_interest = []

    sql = "SELECT * FROM places_of_interest"
    results = run_sql(sql)

    for row in results:
        city = city_repository.select(row['city_id'])
        place_of_interest = PlaceOfInterest(row['name'], row['information'], city, row['visited'], row['id'])
        place_of_interest.append(place_of_interest)
    return places_of_interest

def select(id):
    place_of_interest = None
    sql = "SELECT * FROM places_of_interest WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        city = city_repository.select(result['city_id'])
        place_of_interest = PlaceOfInterest(result['name'], result['information'], city, result['visited'], result['id'])
    return place_of_interest

def delete_all():
    sql = "DELETE  FROM places_of_interest"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM places_of_interest WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(place_of_interest):
    sql = "UPDATE places_of_interest SET (name, information, city, visited) = (%s, %s, %s, %s) WHERE id = %s"
    values = [place_of_interest.name, place_of_interest.information, place_of_interest.city.id, place_of_interest.visited, place_of_interest.id]
    run_sql(sql, values)

def select_all_from_city(city_id):
    places_of_interest=[]

    sql = "SELECT * FROM places_of_interest WHERE city_id = %s"
    values = [city_id]
    results = run_sql(sql, values)

    for row in results:
        city = city_repository.select(city_id)
        place_of_interest = PlaceOfInterest(row['name'], row['information'], city, row['visited'], row['id'])
        places_of_interest.append(place_of_interest)
    return places_of_interest