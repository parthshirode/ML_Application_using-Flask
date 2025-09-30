# Health Insurance Premium Prediction API

This project provides a Flask REST API for training, testing, and predicting health insurance premiums using a linear regression model. The API accepts CSV files or JSON data and returns model evaluation metrics and predictions.

## Features

- Train linear regression model via CSV upload
- Test model with CSV or JSON test data input
- Predict insurance premium by sending JSON feature input

## Technologies Used

- Python 3
- Flask
- Pandas
- scikit-learn

## Setup Instructions

1. Clone the repository.
2. Create and activate a virtual environment (optional but recommended).
3. Install dependencies with:
   ```
   pip install -r requirements.txt
   ```
4. Run the Flask app locally:
   ```
   python app.py
   ```

## API Usage with Postman

### 1. Train Model

- **Method:** POST  
- **URL:** `http://127.0.0.1:5000/train`  
- **Body:** form-data  
- **Key:** `file` (type: File) — Upload your training CSV containing columns `age`, `bmi`, `children`, `sex`, `smoker`, `charges`  
- **Response:**  
  ```json
  {
    "status": "Model trained successfully!"
  }
  ```

***

### 2. Test Model

- **Method:** POST  
- **URL:** `http://127.0.0.1:5000/test`  
- **Body (CSV):** form-data  
- **Key:** `file` (type: File) — Upload test CSV with same columns as training data  

- **OR**

- **Body (JSON):** raw JSON  
- Send JSON with key `"data"` and a list of records as below:

  ```json
  {
    "data": [
      {"age": 25, "bmi": 30.1, "children": 1, "sex": "female", "smoker": "no", "charges": 3200},
      {"age": 40, "bmi": 24.7, "children": 3, "sex": "male", "smoker": "yes", "charges": 15000}
    ]
  }
  ```

- **Response example:**

  ```json
  {
    "r2_score": 0.82,
    "mean_squared_error": 14567.89,
    "mean_absolute_error": 97.45
  }
  ```

***

### 3. Predict Insurance Premium

- **Method:** POST  
- **URL:** `http://127.0.0.1:5000/predict`  
- **Body:** raw JSON  
- **Example JSON:**

  ```json
  {
    "features": [30, 28.1, 2, 1, 0]
  }
  ```

- *Feature Order:* `age`, `bmi`, `children`, `sex_enc` (female=1, male=0), `smoker_enc` (yes=1, no=0)

- **Response example:**

  ```json
  {
    "Predicted Insurance Premium": [12345.67]
  }
  ```

***
