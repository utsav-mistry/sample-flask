from flask import Blueprint

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "<h2>🚀 Welcome to the Flask Dockerized App!</h2>"

@main.route("/about")
def about():
    return "<p>This is a sample containerized Flask app served via ForgeFlow.</p>"
