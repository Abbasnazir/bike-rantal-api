from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('bike_rental_model.pkl')  # This will work now

@app.route('/')
def home():
    return "Bike Rental Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        input_data = np.array([list(data.values())])
        prediction = model.predict(input_data)
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host = "0.0.0.0" , port = 5000)
