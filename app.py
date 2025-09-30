from flask import Flask, jsonify, request
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

app = Flask(__name__)

model = None
X_train = None
y_train = None

def preprocess(df):
     df['sex_enc'] = df['sex'].apply(lambda x:1 if x=='female' else 0)
     df['smoker_enc'] = df['smoker'].map({'yes':1,'no':0})
     return df

@app.route('/train', methods=['POST']) 
def train():
     global model, X_train, y_train
     file = request.files['file']
     df = pd.read_csv(file)
     df = preprocess(df)
     
     X_train = df[['age','bmi','children','sex_enc','smoker_enc']] #X may have multiple columns => DataFrame
     y_train = df['charges']  #y is always single column => Series
     
     model = LinearRegression()
     model.fit(X_train,y_train)
     
     return jsonify({'status':'Model trained successfully!'})
 
@app.route('/test', methods=['POST'])
def test():
    global model
    if model is None:
        return jsonify({'error':'Model not trained yet...'})
    
    file = request.files['file']
    df = pd.read_csv(file)
    df = preprocess(df)

    
    X_test = df[['age','bmi','children','sex_enc','smoker_enc']] #X may have multiple columns => DataFrame
    y_test = df['charges']  #y is always single column => Series
    
    y_pred = model.predict(X_test)
    r2 = model.score(X_test, y_test)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    
    return jsonify({'r2_score':r2,
                    'mean_squaed_error':mse,
                    'mean_absolute_error':mae
                    })
    
@app.route('/predict', methods=['POST'])
def predict():
    global model
    if model is None:
        return jsonify({'error':'Model not trained yet...'})
    
    req_data = request.get_json()
    features = req_data['features']
    
    prediction = model.predict([features])
    return jsonify({'Predicted Insurance Premium':float(prediction[0])})


if __name__ == '__main__':
    app.run(debug = True)
    

    
    