from flask import Blueprint
import os

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "<h2>Welcome to the Flask Dockerized App!</h2>"

@main.route("/about")
def about():
    variable_value = os.getenv("VARIABLE", "Not Set")
    return f"""
        <p>This is a sample containerized Flask app served via ForgeFlow.</p>
        <p>VARIABLE = {variable_value}</p>
    """
