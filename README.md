Capstone Project for Udacity FSND

- Heroku Link: https://jawi13-capstone.herokuapp.com/

Motivation for Project

- This project has been completed as a requirement of the Udacity Full Stack Web Developer Nanodegree. It is the last of 5 projects completed over a 4 month period, and combines the learnings from the first 4 projects.

Project dependencies

- Python 3.7- Download from https://www.python.org/downloads/

Pip dependencies

In a terminal, from the root folder of the project, run:

```

pip install -r requirements.txt

```

This will install the packages required to run the application in your local environment.

Running the server

To run the server, execute the following commands in your terminal:

```

export FLASK_APP=app.py
flask run --reload

```

API Behaviour

Models

- Actor- name (string), age (int), gender (string)-
- Movie- title (string), release year (int)

Roles (Permissions)

- Casting Assistant (GET:actors, GET:movies)
- Casting Director (GET:actors, GET:movies, POST:actors, DELETE:actors, PATCH:actors, PATCH:movies)
- Casting Director (GET:actors, GET:movies, POST:actors, POST:movies, DELETE:actors, DELETE:movies, PATCH:actors, PATCH:movies)

JWT Tokens

Valid JWT tokens are located in the .env file for each role for testing purposes:

- CASTING_ASSISTANT
- CASTING_DIRECTOR
- EXECUTIVE_PRODUCER

If these expire, new tokens can be gathered by visting this link:

Https://jawi13.eu.auth0.com/authorize?audience=capstone&response_type=token&client_id=z16veMHKK3vG12c7y4x05GpitpqOVK5p&redirect_uri=https://capstone/callback

Use the following login details for test accounts to retrieve the tokens:

- Casting Assistant: 
    - email: assistant@test.com
    - password: Assistant1

- Casting Director:
    - email: director@test.com
    - password: Director1

- Executive Producer:
    - email: producer@test.com
    - password: Producer1

Endpoints

There are two API endpoints, one for each model, Actor and Movie. Each endpoint allows GET, POST, DELETE and PATCH methods. Remember to include a valid JWT Bearer token with the correct permissions in the request header for the request to be successful.

GET 'actors'

- response:

```

{
  "actors": {
    "1": {
      "age": 42,
      "gender": "Male",
      "id": 1,
      "name": "Tom Hardy"
    },
    "2": {
      "age": 37,
      "gender": "Female",
      "id": 2,
      "name": "Anne Hathaway"
    }
  },
  "success": true
}

```

POST 'actors'

- request body:

```

{
"age": 37,
"name": "Anne Hathaway",
"gender": "Female"
}

```

- response:

```

{
  "actor": {
    "age": 37,
    "gender": "Female",
    "id": 2,
    "name": "Anne Hathaway"
  },
  "success": true
}

```

DELETE 'actors/<int:actor_id>'

- response:

```

{
  "deleted": 3,
  "success": true
}

```

PATCH 'actors/<int:actor_id>'

- request body:

```

{
"age": 37,
"name": "Anne Hathaway",
"gender": "Female"
}

```

- response:

```

{
  "actor": {
    "age": 37,
    "gender": "Female",
    "id": 2,
    "name": "Anne Hathaway"
  },
  "success": true
}

```

GET 'movies'

- response:

```

{
  "movies": {
    "1": {
      "id": 1,
      "release_year": 2009,
      "title": "Avatar"
    },
    "2": {
      "id": 2,
      "release_year": 2019,
      "title": "Joker"
    }
  },
  "success": true
}

```

POST 'movies'

- request body:

```

{
"release_year": 2019,
"title": "Joker"
}

```

- response:

```

{
  "movie": {
    "id": 2,
    "release_year": 2019,
    "title": "Joker"
  },
  "success": true
}

```

DELETE 'movies/<int:movie_id>'

- response:

```

{
  "deleted": 3,
  "success": true
}

```

PATCH 'movies/<int:movie_id>'

- request body:

```

{
"release_year": 2019,
"title": "Joker"
}

```

- response:

```

{
  "movie": {
    "id": 2,
    "release_year": 2019,
    "title": "Joker"
  },
  "success": true
}

```

Testing

To run the unit tests, from the root folder of the project directory, run in your terminal:

```

python test_app.py

```