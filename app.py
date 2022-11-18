import os
from flask import (
    Flask, flash, render_template, 
    redirect, session, url_for) 
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_opportunities")
def get_opportunities():
    opportunities = list(mongo.db.opportunities.find())
    opportunity = mongo.db.opportunities.find_one()
    print(opportunities)
    print(opportunity)
    return render_template("opportunities.html", opportunities=opportunities, opportunity=opportunity)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)