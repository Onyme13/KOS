# Generate a simple flask app
from flask import Flask, render_template, request
from flask_socketio import SocketIO
from queries import *
import re

app = Flask(__name__)
socketio = SocketIO(app)


# SocketIO connection
@socketio.on('connect')
def connect():
    print('connection established')

# SocketIO disconnection
@socketio.on('disconnect')
def disconnect():
    print('disconnected')

@app.route('/')
def index():
    aircraft_list = []
    all_aircraft = get_all_aircraft()
    pattern = r"urn:ngsi-ld:(.*)"

    for aircraft in all_aircraft:
        aircraft_id = aircraft['id']
        aircraft_id = re.sub(pattern, r"\1", aircraft_id)
        aircraft_list.append(aircraft_id)


    aircraft = request.args.get('aircraft')
    return render_template('index.html', aircraft_list=aircraft_list)


@app.route('/aircraft')
def aircraft():
    aircraft = request.args.get('aircraft')
    print(aircraft)


    if aircraft == "Aircraft:001":
        temperature = '72°C'
        vibration = '0.4'
    elif aircraft == "Aircraft:002":
        temperature = '75°C'
        vibration = '0.5'
    return render_template('aircraft.html',aircraft=aircraft,temperature1=temperature, vibration1=vibration)





if __name__ == '__main__':
    app.run(debug=True)