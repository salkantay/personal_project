from app import app
from flask import render_template

@app.route('/')
def home_page():
    return render_template('home-page.html')

@app.route('/about')
def about_page():
    return render_template('about.html')