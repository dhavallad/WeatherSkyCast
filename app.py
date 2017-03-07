# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for
from geolocation.main import GoogleMaps
import requests,json
import datetime
import numpy as np
import csv
from itertools import izip


# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/', methods=['GET'])
def form():
    return render_template('form_submit.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/home', methods=['POST'])
def hello():
    email=request.form['youremail']
    return render_template('home.html', name=email)

@app.route('/qwe', methods=['POST'])
def qwe():
	#name= request.form['uname']
	#print "Hi"
	address=request.form['addr']
	google_maps = GoogleMaps(api_key='AIzaSyBCCeBBAs_GOkEphWvfpdw0VaeR-SrH-F4') 

	location = google_maps.search(location=address) # sends search to Google Maps.
	my_location = location.first()
	#print(my_location.lat)
	#print(my_location.lng)
	url = "https://api.darksky.net/forecast/63ba9bb3c3e8270e19c1f1b27a81d090/" + str(my_location.lat) + "," + str(my_location.lng)
	#print url
	r = requests.get(url)
	parseString = json.loads(r.text)

	current= parseString['currently']
	t= parseString['hourly']
	list1=t['data']
	curr= parseString['currently']
	#print curr
