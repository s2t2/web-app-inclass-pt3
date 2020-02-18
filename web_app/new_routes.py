

from flask import Blueprint, jsonify, request, render_template, flash

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
    try:
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
        statuses = client.user_timeline(screen_name, tweet_mode="extended", count=200, exclude_replies=True, include_rts=False)
        for status in statuses:
            print(status.full_text)
            # Find or create database tweet:
            db_tweet = Tweet.query.get(status.id) or Tweet(id=status.id)
            print(db_tweet)
            # Update database tweet:
            db_tweet.user_id = status.author.id # or db_user.id
            db_tweet.full_text = status.full_text
            db.session.add(db_tweet)
        db.session.commit()

        return render_template("user_profile.html", user=db_user, tweets=db_user.tweets)
    except Exception as e:
        print(e)
        return jsonify({"message": "OOPS THERE WAS AN ERROR. PLEASE TRY ANOTHER USER."})

@new_routes.route("/reset")
def reset():
    db.drop_all()
    db.create_all()
    return jsonify({"message": "Database Reset OK"})




@new_routes.route("/train")
def train():
    print("TRAINING THE MODEL...")


    return jsonify({"message": "Model trained and saved."})

@new_routes.route("/predict", methods=["POST"])
def predict():
    print("LOADING THE MODEL...")

    print("PREDICTING...")
    print("FORM DATA:", dict(request.form))
    return render_template("results.html", prediction_results="TODO")
