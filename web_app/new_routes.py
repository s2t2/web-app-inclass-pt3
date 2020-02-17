

from flask import Blueprint, jsonify, request, render_template

from web_app.models import User, Tweet, db
from web_app.twitter_service import twitter_api_client

new_routes = Blueprint("new_routes", __name__)

client = twitter_api_client()

@new_routes.route("/")
def index():
    return render_template("homepage.html")

@new_routes.route("/users")
@new_routes.route("/users.json")
def list_users():
    print("LISTING USERS...")
    users = User.query.all() # returns a list of <class 'alchemy.User'>
    print(len(users))

    users_response = []
    for u in users:
        user_dict = u.__dict__
        del user_dict["_sa_instance_state"]
        users_response.append(user_dict)

    return jsonify(users_response)

@new_routes.route("/users/<string:screen_name>")
def show_user(screen_name=None):
    print("SHOWING USER:", screen_name)

    # Get user info from twitter:
    twitter_user = client.get_user(screen_name)
    print(type(twitter_user))

    # Find or create database user:
    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)
    print(db_user)
    # Update database user:
    db_user.screen_name = twitter_user.screen_name
    db_user.followers_count = twitter_user.followers_count
    db.session.add(db_user)
    db.session.commit()

    # Get Tweets:


    #if db_user:
    #    db_user = User(id=tw_user.id, screen_name=tw_user.screen_name, followers_count=tw_user.followers_count)
    #    db.session.add(db_user)



    #breakpoint()

    #db_user = (
    #    User.query.get(twitter_user.id) or
    #
    #)



    #tweet_mode="extended"
    #count=200,
    #exclude_replies=True,
    #include_rts=False


    return render_template("user_profile.html", screen_name=screen_name)





@new_routes.route("/predict", methods=["POST"])
def predict():
    print("PREDICTING...")
    print("FORM DATA:", dict(request.form))
    return render_template("results.html", prediction_results="TODO")
