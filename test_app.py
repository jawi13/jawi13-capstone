import os
import unittest
import json
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie

# load .env file
load_dotenv()

# define and initiate the test case


class CapstoneTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.assistant = os.getenv('CASTING_ASSISTANT')
        self.director = os.getenv('CASTING_DIRECTOR')
        self.producer = os.getenv('EXECUTIVE_PRODUCER')
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app)

        self.new_actor = {
            'name': 'Daniel Craig',
            'age': '52',
            'gender': 'Male',
        }

        self.new_movie = {
            'title': 'Die Hard',
            'release_year': 1988
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

# test GET for actors as casting assistant

    def test_get_actors_assistant(self):

        response = self.client().get(
            '/actors', headers={"Authorization":
                                "Bearer {}".format(self.assistant)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

# test GET for actors failure

    def test_get_actors_failure(self):

        response = self.client().get('/actors')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)

# test GET for movies as casting assistant

    def test_get_movies_assistant(self):

        response = self.client().get(
            '/movies', headers={"Authorization":
                                "Bearer {}".format(self.assistant)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

# test GET for movies failure

    def test_get_movies_failure(self):

        response = self.client().get('/movies')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)

# test POST for actors as casting director

    def test_post_actor_director(self):

        actors_before = Actor.query.all()

        response = self.client().post('/actors', json=self.new_actor,
                                      headers={"Authorization":
                                               "Bearer {}"
                                               .format(self.director)})
        data = json.loads(response.data)

        actors_after = Actor.query.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(actors_after) - len(actors_before) == 1)

# test POST failure for actors as casting assistant

    def test_post_actor_failure_assistant(self):

        actors_before = Actor.query.all()

        response = self.client().post('/actors', json=self.new_actor,
                                      headers={"Authorization":
                                               "Bearer {}"
                                               .format(self.assistant)})
        data = json.loads(response.data)

        actors_after = Actor.query.all()

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertTrue(len(actors_after) == len(actors_before))

# test POST for movies as executive producer

    def test_post_movie_producer(self):

        movies_before = Movie.query.all()

        response = self.client().post('/movies', json=self.new_movie,
                                      headers={"Authorization":
                                               "Bearer {}"
                                               .format(self.producer)})
        data = json.loads(response.data)

        movies_after = Movie.query.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(movies_after) - len(movies_before) == 1)

# test POST failure for movies as executive producer

    def test_post_movie_failure_producer(self):

        movies_before = Movie.query.all()

        response = self.client().post('/movies', json={},
                                      headers={"Authorization":
                                               "Bearer {}"
                                               .format(self.producer)})
        data = json.loads(response.data)

        movies_after = Movie.query.all()

        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertTrue(len(movies_after) == len(movies_before))

# test PATCH for actors as casting director

    def test_patch_actor_director(self):

        actors_before = Actor.query.all()

        response = self.client().patch('/actors/1', json=self.new_actor,
                                       headers={"Authorization":
                                                "Bearer {}"
                                                .format(self.director)})
        data = json.loads(response.data)

        actors_after = Actor.query.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(actors_before) == len(actors_after))

# test PATCH failure for actors as casting director

    def test_patch_actor_failure_director(self):

        actors_before = Actor.query.all()

        response = self.client().patch('/actors/1', json={},
                                       headers={"Authorization":
                                                "Bearer {}"
                                                .format(self.director)})
        data = json.loads(response.data)

        actors_after = Actor.query.all()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(len(actors_before) == len(actors_after))

# test PATCH for movies as casting director

    def test_patch_movie_director(self):

        movies_before = Movie.query.all()

        response = self.client().patch('/movies/8', json=self.new_movie,
                                       headers={"Authorization":
                                                "Bearer {}"
                                                .format(self.director)})
        data = json.loads(response.data)

        movies_after = Movie.query.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(movies_before) == len(movies_after))

# test PATCH failure for movies as casting director

    def test_patch_movie_failure_director(self):

        movies_before = Movie.query.all()

        response = self.client().patch('/movies/1', json={},
                                       headers={"Authorization":
                                                "Bearer {}"
                                                .format(self.director)})
        data = json.loads(response.data)

        movies_after = Movie.query.all()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(len(movies_before) == len(movies_after))


if __name__ == "__main__":
    unittest.main()
