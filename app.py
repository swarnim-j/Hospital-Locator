from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hospitals', methods=['POST'])
def hospitals():
    user_location = request.form['user_location']
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": user_location,
        "radius": "10000",
        "type": "hospital",
        "key": "YOUR_API_KEY"
    }
    response = requests.get(url, params=params)
    results = json.loads(response.text)['results']
    return render_template('hospitals.html', results=results)

if __name__ == '__main__':
    app.run()
