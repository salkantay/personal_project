from app import app
from flask import render_template, redirect, url_for, request
import requests
import json

@app.route('/')
def home_page():
    return render_template('home-page.html')

@app.route('/food_hygiene', methods=['GET', 'POST'])
def food_hygiene():

    business_types = []
    if request.method == 'GET':

        headers = {}
        # url = 'https://ratings.food.gov.uk/OpenDataFiles/FHRS416en-GB.json'
        # url = 'https://ratings.food.gov.uk/enhanced-search/en-GB/^/^/DISTANCE/0/^/1.5907/54.9840/1/30/json'
        url = 'https://ratings.food.gov.uk/business-types/json'
        headers['content-type'] = 'application/json'

        loading = requests.get(url, headers=headers, verify=False)
        loading = loading.json()
        print(loading)
        for key in loading['ArrayOfWebBusinessTypeAPI']['WebBusinessTypeAPI']:
            business_types.append(key['BusinessTypeName'])
        # print(loading['ArrayOfWebBusinessTypeAPI']['WebBusinessTypeAPI']['BusinessTypeName'])

        print(business_types)

        return render_template('food-hygiene.html',
                                business_types=business_types)