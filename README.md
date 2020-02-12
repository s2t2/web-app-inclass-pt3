# inclass-web-app-2

## Setup

```sh
pipenv install --python 3.7

pipenv install Flask Flask-SQLAlchemy Flask-Migrate
```


```sh
cd web_app

FLASK_APP=app.py flask db init #> generates app/migrations dir

# run both when changing the schema:
FLASK_APP=app.py flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=app.py flask db upgrade #> creates the "users" table
```


## Run

```sh
FLASK_APP=app.py flask run
```
