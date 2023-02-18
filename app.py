from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hospitals', methods=['POST'])
def hospitals():
    lat = request.form['latitude']
    lng = request.form['longitude']
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius=10000&type=hospital&key=YOUR_API_KEY"
    response = requests.get(url)
    data = response.json()
    hospitals = []
    for result in data['results']:
        hospitals.append({'name': result['name'], 'phone': result.get('formatted_phone_number', 'Phone number not available'), 'address': result.get('vicinity', 'Address not available')})
    return render_template('hospitals.html', hospitals=hospitals)

if __name__ == '__main__':
    app.run(debug=True)
