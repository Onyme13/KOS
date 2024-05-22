from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from threading import Thread, Event
from queries import *
import re
import json
import time
from data_simulation_engine import *

app = Flask(__name__)
socketio = SocketIO(app)


current_aircraft = None  # Global variable to store the current aircraft


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

    return render_template('index.html', aircraft_list=aircraft_list)

@app.route('/aircraft')
def aircraft():
    global current_aircraft
    current_aircraft = request.args.get('aircraft')
    pattern = r"urn:ngsi-ld:(.*)"

    engine_data = []

    # Get all the engines linked to the aircraft
    engines = get_engines_linked_to_aircraft(current_aircraft)
    
    if engines:
        for engine in engines:
            data = get_engine_data(engine['id'])
            if data:

                engine_data.append({
                    "engine": re.sub(pattern,r"\1" ,engine['id']),
                    "vibration": data[-2]['vibrationValue']['value'],
                    "temperature": data[-1]['temperatureValue']['value']
                })
    else:
        return "Error retrieving engines"
    
    return render_template('aircraft.html', aircraft=current_aircraft, engine_data=engine_data)

@app.route('/aircraft_data')
def aircraft_data():
    aircraft = request.args.get('aircraft')

    aircraft_data = get_aircraft(aircraft)


    return render_template('aircraft_data.html', aircraft=aircraft_data)

@app.route('/engine_data')
def engine_data():
    engine = request.args.get('engine')

    engine_data = get_engine(engine)
    
    if engine_data is None:
        return "Error retrieving engine data"

    return render_template('engine_data.html', engine=engine_data)






# Thread for emitting engine data every 5 seconds
def emit_engine_data_periodically():
    while not stop_event.is_set():

        engines = get_engines_linked_to_aircraft(current_aircraft)
        engine_data = []
        if current_aircraft:
            engines = get_engines_linked_to_aircraft(current_aircraft)
            engine_data = []
            if engines:
                for engine in engines:
                    data = generate_data() #get_engine_data(engine['id'])
                    #data =  get_engine_data(engine['id']) #generate_data()
                    #print(data)
                    if data:
                        engine_data.append({
                            "engine": re.sub(r"urn:ngsi-ld:(.*)", r"\1", engine['id']),
                            "vibration": data[-2]['vibrationValue']['value'],
                            "temperature": data[-1]['temperatureValue']['value']
                        })
            socketio.emit('update_engine_data', engine_data)
            time.sleep(5)





if __name__ == '__main__':
    stop_event = Event()
    thread = Thread(target=emit_engine_data_periodically)
    thread.start()
    try:
        socketio.run(app)
    finally:
        stop_event.set()
        thread.join()