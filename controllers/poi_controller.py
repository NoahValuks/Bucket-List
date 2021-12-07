import re
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.poi import PlaceOfInterest
import repositories.poi_repository as poi_repository
import repositories.city_repository as city_repository

poi_blueprint = Blueprint("poi", __name__)

@poi_blueprint.route('/poi/new')
def new_poi():
    cities = city_repository.select_all()
    return render_template("/poi/new_poi.html", cities = cities)

@poi_blueprint.route("/poi/create", methods = ['POST'])
def create_poi():
    name = request.form['name']
    information = request.form['information']
    city_id = request.form['city_id']
    visited = request.form['visited']
    city = city_repository.select(city_id)
    poi = PlaceOfInterest(name, information, city, visited)
    poi_repository.save(poi)
    return redirect(f"/cities/{city_id}")

@poi_blueprint.route('/poi/<id>/edit')
def edit_poi(id):
    place = poi_repository.select(id)
    cities = city_repository.select_all()
    return render_template('/poi/edit.html', place = place, cities = cities)

@poi_blueprint.route("/poi/update/<id>", methods = ['POST'])
def update_poi(id):
    name = request.form['name']
    information = request.form['information']
    city_id = int(request.form['city_id'])
    visited = request.form['visited']
    city = city_repository.select(city_id) 
    poi = PlaceOfInterest(name, information, city, visited, id)
    poi_repository.update(poi)
    return redirect(f"/cities/{city_id}")

@poi_blueprint.route("/poi/<city_id>/<place_id>/delete", methods = ['POST'])
def delete_poi(city_id, place_id):
    poi_repository.delete(place_id)
    return redirect(f"/cities/{city_id}")
