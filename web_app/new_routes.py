

from flask import Blueprint, jsonify, request, render_template

from web_app.models import User, Tweet, db
from web_app.twitter_service import twitter_api_client

new_routes = Blueprint("new_routes", __name__)

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
    print("SHOWING USER...")
    print("REQUEST PARAMS:", dict(request.args))
    print(screen_name)

    #if "screen_name" in request.args:
    #    name = request.args["name"]
    #    message = f"Hello, {name}"
    #else:
    #    message = "Hello World"


    #return message
    return render_template("user_profile.html", screen_name=screen_name)





@new_routes.route("/predict", methods=["POST"])
def predict():
    print("PREDICTING...")
    print("FORM DATA:", dict(request.form))
    return render_template("results.html", prediction_results="TODO")
