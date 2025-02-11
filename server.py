from flask import Flask, jsonify, render_template
from drone_class import Drone
import random

app = Flask(__name__)

random_drone = Drone( #drone class is initialised with random values
                        [random.randint(0, 100), random.randint(0, 100)],
                        random.randint(10, 100),
                        random.randint(0, 20)
)

@app.route('/')
def home():
    return render_template("display.html")  # Looks inside 'templates' folder

@app.route('/drone-data')
def drone_data():
    random_drone.update_position()  # Update values before sending response
    return jsonify(random_drone.retrieve_data())

if __name__ == '__main__':
    app.run(debug=True)