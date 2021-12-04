from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.place_of_interest_repository as place_of_interest_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route('/cities/new')
def new_city():
    countries = country_repository.select_all()
    return render_template("/cities/new_city.html", countries = countries)

@cities_blueprint.route("/cities", methods = ['POST'])
def create_city():
    name = request.form['name']
    country_id = request.form['country_id']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city = City(name, country, visited)
    city_repository.save(city)
    return redirect(f"/countries/{country_id}")

@cities_blueprint.route('/countries/cities/<id>')
def show_city(id):
    city = city_repository.select(id)
    places = place_of_interest_repository.select_all_from_city(id)
    return render_template('/cities/index.html', city=city, places = places)

@cities_blueprint.route('/countries/cities/<id>/edit')
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template('/cities/edit.html', city = city, countries = countries)

@cities_blueprint.route("/countries/cities/<id>/update", methods= ['POST'])
def update_city(id):
    name = request.form['name']
    country_id = int(request.form['country_id'])
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city = City(name, country, visited, id)
    city_repository.update(city)
    return redirect(f"/countries/cities/{city.id}")

@cities_blueprint.route("/countries/cities/<id>/delete", methods = ['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect("/countries")