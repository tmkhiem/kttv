import datetime
import random
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/flood")
def get_flood_data():
    location_id = request.args.get('location')
    timestamp = request.args.get('timestamp')
    if timestamp is None: timestamp = datetime.datetime.now()

    return  {
                'location': location_id,
                'timestamp': timestamp.isoformat(),
                'flood': random.randint(0,4)
            }

@app.route("/rain") 
def get_rain_data():
    location_id = request.args.get('location')
    timestamp = request.args.get('timestamp')
    if timestamp is None: timestamp = datetime.datetime.now()

    return  {
                'location': location_id,
                'timestamp': timestamp.isoformat(),
                'rain': random.randint(0,4)
            }

@app.route("/level")
def get_level_reading():
    location_id = request.args.get('location')
    timestamp = request.args.get('timestamp')
    if timestamp is None: timestamp = datetime.datetime.now()

    return  {
                'location': location_id,
                'timestamp': timestamp.isoformat(),
                'level': random.randint(-111,111)
            }