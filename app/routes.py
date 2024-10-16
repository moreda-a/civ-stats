from flask import Blueprint

# Define a blueprint
main = Blueprint('main', __name__)

@main.route('/')
def hello():
    return "Hello World 2!"