from flask import Blueprint, render_template, request
from os import getenv

main = Blueprint("main", __name__)

@main.route('/')
def home():
    env_data = {
        'environment': getenv('ENVIRONMENT', 'development'),
        'version': getenv('APP_VERSION', '0.0.0'),
        'platform_name': getenv('PLATFORM_NAME', 'Platform')
    }
    return render_template('home.html', env=env_data)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
    return render_template('contact.html')
