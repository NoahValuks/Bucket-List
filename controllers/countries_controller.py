from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries = countries)

@countries_blueprint.route("/countries/<id>")
def show_cities(id):
    cities = city_repository.select_all_from_country(id)
    country = country_repository.select(id)
    return render_template("countries/show_cities.html", cities=cities, country=country)

@countries_blueprint.route('/countries/new')
def new_country():
    return render_template("/countries/new_country.html")

@countries_blueprint.route("/countries", methods = ['POST'])
def create_country():
    name = request.form['name']
    capital = request.form['capital']
    visited = request.form['visited']
    country = Country(name, capital, visited)
    country_repository.save(country)
    return redirect("/countries")

@countries_blueprint.route('/countries/<id>/edit')
def edit_country(id):
    country = country_repository.select(id)
    return render_template('/countries/edit.html', country = country)

@countries_blueprint.route("/countries/<id>", methods= ['POST'])
def update_country(id):
    name = request.form['name']
    capital = request.form['capital']
    visited = request.form['visited']
    country = Country(name, capital, visited, id)
    country_repository.update(country)
    return redirect(f"/countries/{country.id}")

@countries_blueprint.route("/countries/<id>/delete", methods = ['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect("/countries")