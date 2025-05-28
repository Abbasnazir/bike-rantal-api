# Bike Rental Prediction API

This project provides a machine learning API to predict the number of bike rentals using a trained Random Forest model.

## Features
- Accepts input data via POST request
- Predicts bike rental count
- Built with Flask
- Tested using Postman

##  Requirements

Install dependencies using :
pip install -r requirements.txt
# Run the API 
# start the flask server locally by running : 
python app.py

# This will start the server at :
http://127.0.0.1:5000

---
---
---

##  API Endpoint

**POST** 'http://127.0.0.1:5000/predict'

### Example JSON Input

`json
{
  "season": 1,
  "yr": 1,
  "mnth": 1,
  "holiday": 0,
  "weekday": 6,
  "workingday": 0,
  "weathersit": 2,
  "temp": 0.2,
  "atemp": 0.212,
  "hum": 0.8,
  "windspeed": 0.1
}
## Sample json output
{ 
    " predection": 1710.68

}