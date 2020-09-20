from app import app
from flask import render_template, redirect, url_for, request
import requests
import json

@app.route('/')
def home_page():
    return render_template('home-page.html')

@app.route('/food_hygiene', methods=['GET', 'POST'])
def food_hygiene():
    if request.method == 'GET':

        headers = {}
        # url = 'https://ratings.food.gov.uk/OpenDataFiles/FHRS416en-GB.json'
        url = 'https://ratings.food.gov.uk/enhanced-search/en-GB/^/^/DISTANCE/0/^/1.5907/54.9840/1/30/json'
        headers['content-type'] = 'application/json'

        loading = requests.get(url, headers=headers, verify=False)
        loading = loading.json()
        print(loading)
        # print(loading['FHRSEstablishment']['EstablishmentCollection']['EstablishmentDetail']['BusinessName'])

        return render_template('food-hygiene.html')