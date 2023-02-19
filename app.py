from flask import Flask, render_template, request
import requests
import os
from flask import current_app

app = Flask(__name__)

app.config['GOOGLE_MAPS_API_KEY'] = os.environ['GOOGLE_MAPS_API_KEY']
radius = 10000

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hospitals', methods=['POST'])
def hospitals():
    with current_app.app_context():
        api_key = current_app.config['GOOGLE_MAPS_API_KEY']
        lat = request.form['latitude']
        lng = request.form['longitude']
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type=hospital&key={api_key}"
        response = requests.get(url)
        data = response.json()
        hospitals = []
        for result in data['results']:
            print(result)
            hospitals.append({'name': result['name'], 'address': result.get('vicinity', 'Address not available')})
        return render_template('hospitals.html', hospitals=hospitals)

if __name__ == '__main__':
    app.run(debug=True)