from flask import Flask, render_template, request
from os import getenv
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

app = Flask(__name__)

@app.route('/')
def home():
    env_data = {
        'environment': getenv('ENVIRONMENT', 'development'),
        'version': getenv('APP_VERSION', '0.0.0'),
        'platform_name': getenv('PLATFORM_NAME', 'Platform')
    }
    return render_template('home.html', env=env_data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Here you can add code to handle the form submission
        # For now, it just renders the template
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
