import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Actor, Movie
from auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app, resources={"/": {"origins": "*"}})

  @app.after_request
  def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, PUT, POST, DELETE, OPTIONS')
        return response

  @app.route('/actors')
  @requires_auth('get:actors')
  def get_actors(self):
      actors = Actor.query.all()
      actors_dict = {}
      for actor in actors:
          actors_dict[actor.id] = actor.format()

      if (len(actors_dict) == 0):
          abort(404)

      return jsonify({
          'success': True,
          'actors': actors_dict
      })

  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actors')
  def post_actor(self):
      body = request.get_json()

      new_name = body.get('name')
      new_age = body.get('age')
      new_gender = body.get('gender')

      if ((new_name is None)) or (new_age is None) or (new_gender is None):
          abort(422)

      try:
          actor = Actor(name=new_name, age=new_age, gender=new_gender)
          actor.insert()
          new_actor = actor.format()
          return jsonify({
              'success': True,
              'actor': new_actor,
          }), 200

      except Exception:
          abort(422)
  
  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actor(self, actor_id):
      actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

      if actor is None:
        abort(404)

      actor.delete()

      return jsonify({
        'success': True,
        'deleted': actor_id
      }), 200
  
  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  @requires_auth('patch:actors')
  def edit_actor(self, actor_id):
      actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

      if actor is None:
        abort(404)
      
      body = request.get_json()
      if body is None:
        abort(404)

      new_name = body.get('name')
      new_age = body.get('age')
      new_gender = body.get('gender')

      try:
        if new_name is not None:
          actor.name = new_name

        if new_age is not None:
          actor.age = new_age

        if new_gender is not None:
          actor.gender = new_gender

        actor.update()

        new_actor = actor.format()

        return jsonify({
          'success': True,
          'actor': new_actor
        }), 200

      except Exception:
        abort(422)

  @app.route('/movies')
  @requires_auth('get:movies')
  def get_movies(self):
      movies = Movie.query.all()
      movies_dict = {}
      for movie in movies:
          movies_dict[movie.id] = movie.format()

      if (len(movies_dict) == 0):
          abort(404)

      return jsonify({
          'success': True,
          'movies': movies_dict
      })

  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movies')
  def post_movie(self):
      body = request.get_json()

      new_title = body.get('title')
      new_release_year = body.get('release_year')

      if ((new_title is None)) or (new_release_year is None):
          abort(422)

      try:
          movie = Movie(title=new_title, release_year=new_release_year)
          movie.insert()
          new_movie = movie.format()
          return jsonify({
              'success': True,
              'movie': new_movie,
          }), 200

      except Exception:
          abort(422)
  
  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movie(self, movie_id):
      movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

      if movie is None:
        abort(404)

      movie.delete()

      return jsonify({
        'success': True,
        'deleted': movie_id
      }), 200
  
  @app.route('/movies/<int:movie_id>', methods=['PATCH'])
  @requires_auth('patch:movies')
  def edit_movie(self, movie_id):
      movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

      if movie is None:
        abort(404)
      
      body = request.get_json()
      if body is None:
        abort(404)

      new_title = body.get('title')
      new_release_year = body.get('release_year')

      try:
        if new_title is not None:
          movie.title = new_title

        if new_release_year is not None:
          movie.release_year = new_release_year

        movie.update()

        new_movie = movie.format()

        return jsonify({
          'success': True,
          'movie': new_movie
        }), 200

      except Exception:
        abort(422)
  
  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
          "success": False,
          "error": 404,
          "message": "resource not found"
      }), 404

  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
          "success": False,
          "error": 422,
          "message:": "unprocessable"
      }), 422

  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
          "success": False,
          "error": 400,
          "message:": "bad request"
      }), 400

  @app.errorhandler(401)
  def unauthorized(error):
      return jsonify({
          "success": False,
          "error": 401,
          "message": "unauthorized"
      }), 401

  @app.errorhandler(405)
  def method_not_allowed(error):
      return jsonify({
          "success": False,
          "error": 405,
          "message": "method not allowed"
      }), 405

  @app.errorhandler(500)
  def internal_server_error(error):
      return jsonify({
          "success": False,
          "error": 500,
          "message:": "internal server error"
      }), 500

  @app.errorhandler(AuthError)
  def auth_error(error):
      return jsonify({
          'success': False,
          'error': error.status_code,
          'message': error.error['description']
      }), error.status_code

  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)