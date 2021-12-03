from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route('/cities/new')
def new_city():
    countries = country_repository.select_all()
    return render_template("/cities/new_city.html", countries = countries)

@cities_blueprint.route("/cities", methods = ['POST'])
def create_city():
    name = request.form['name']
    country_id = request.form['country_id']
    places_of_interest = request.form['places_of_interest']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city = City(name, country, places_of_interest, visited)
    city_repository.save(city)
    return redirect(f"/countries/{country_id}")

@cities_blueprint.route('/countries/cities/<id>')
def show_city(id):
    city = city_repository.select(id)
    return render_template('/cities/index.html', city=city)

@cities_blueprint.route('/countries/cities/<id>/edit')
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template('/cities/edit.html', city = city, countries = countries)
