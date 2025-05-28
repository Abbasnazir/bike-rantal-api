from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(name)
model = joblib.load("bike_rental_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        data = [
            float(request.form["season"]),
            float(request.form["yr"]),
            float(request.form["mnth"]),
            float(request.form["holiday"]),
            float(request.form["weekday"]),
            float(request.form["workingday"]),
            float(request.form["weathersit"]),
            float(request.form["temp"]),
            float(request.form["atemp"]),
            float(request.form["hum"]),
            float(request.form["windspeed"])
        ]
        features = np.array([data])
        prediction = model.predict(features)
        return render_template("index.html", prediction=round(prediction[0], 2))
