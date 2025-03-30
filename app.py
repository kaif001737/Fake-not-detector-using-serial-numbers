from flask import Flask, render_template, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__, template_folder="templates")  # Ensure Flask knows where to find templates
CORS(app)

# Load dataset
df = pd.read_csv("serial_numbers.csv")
real_serials = set(df["Serial Number"])

# Serve the index.html page
@app.route('/')
def home():
    return render_template('index.html')  # Flask automatically looks in the 'templates/' folder

# API to check serial numbers
@app.route('/check_serial/<string:serial_number>', methods=['GET'])
def check_serial(serial_number):
    if serial_number in real_serials:
        return jsonify({"serial_number": serial_number, "status": "real"})
    else:
        return jsonify({"serial_number": serial_number, "status": "fake"}), 404

if __name__ == '__main__':
    app.run(debug=True)
