from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.place_of_interest import PlaceOfInterest
import repositories.place_of_interest_repository as place_of_interest_repository
import repositories.city_repository as city_repository

poi_blueprint = Blueprint("points_of_interest", __name__)

@poi_blueprint.route('/cities/place_of_interest/new')
def new_place_of_interest():
    cities = city_repository.select_all()
    return render_template("/poi/new_poi.html", cities = cities)

@poi_blueprint.route("/cities/place_of_interest/create", methods = ['POST'])
def create_place_of_interest():
    name = request.form['name']
    information = request.form['information']
    city_id = request.form['city_id']
    visited = request.form['visited']
    city = city_repository.select(city_id)
    place_of_interest = PlaceOfInterest(name, information, city, visited)
    place_of_interest_repository.save(place_of_interest)
    return redirect(f"/countries/cities/{city_id}")

@poi_blueprint.route('/cities/place_of_interest/<id>/edit')
def edit_poi(id):
    place_of_interest = place_of_interest_repository.select(id)
    cities = city_repository.select_all()
    return render_template('/cities/edit.html', place_of_interest = place_of_interest, cities = cities)