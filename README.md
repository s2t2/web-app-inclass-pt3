# inclass-web-app-2

## Setup

Setup virtual environment:

```sh
pipenv install --python 3.7

pipenv install Flask Flask-SQLAlchemy Flask-Migrate # night 1
pipenv install python-dotenv requests tweepy basilica # night 2
pipenv install scikit-learn # night 3

pipenv shell
```

Setup database:

```sh
FLASK_APP=web_app flask db init #> generates app/migrations dir

# run both when changing the schema:
FLASK_APP=web_app flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=web_app flask db upgrade #> creates the "users" table
```


## Run

Run the app:

```sh
FLASK_APP=web_app flask run
```

## Deploy

```sh
pipenv install gunicorn psycopg2-binary
```

```sh
heroku create
#> https://desolate-tundra-53293.herokuapp.com/ | https://git.heroku.com/desolate-tundra-53293.git

heroku addons:create heroku-postgresql:hobby-dev
#> provisions a new DATABASE_URL

heroku config
heroku config:set TWITTER_API_KEY="_____"
heroku config:set TWITTER_API_SECRET="______"
heroku config:set TWITTER_ACCESS_TOKEN="______"
heroku config:set TWITTER_ACCESS_TOKEN_SECRET="_____"
heroku config:set BASILICA_API_KEY="______"
heroku config

git push heroku prep-4-deploy:master
```

```sh
heroku run bash
# ... python --version
# ... python web_app/stocks_service.py

heroku run "python web_app/stocks_service.py"

heroku run "FLASK_APP=web_app flask db init"
heroku run "FLASK_APP=web_app flask db stamp head"
heroku run "FLASK_APP=web_app flask db migrate"
heroku run "FLASK_APP=web_app flask db upgrade"

heroku open

heroku logs --tail
```
