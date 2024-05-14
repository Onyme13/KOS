# Generate a simple flask app
from flask import Flask, render_template, request
from flask_socketio import SocketIO
from queries import *

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
    aircraft = request.args.get('aircraft')
    return render_template('index.html')


@app.route('/aircraft')
def aircraft():
    aircraft = request.args.get('aircraft')
    print(aircraft)
    # Get the engine data
    #engine1_data = engine("001")
    #engine2_data = engine("002")
    #engine3_data = engine("003")
    #engine4_data = engine("004")

    aircraft ="yyy"

    temperature = '72°C'
    vibration = '0.4'
    return render_template('aircraft.html',aircraft=aircraft,temperature1=temperature, vibration1=vibration)





if __name__ == '__main__':
    app.run(debug=True)