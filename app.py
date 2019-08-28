import numpy as np
import pandas as pd
import json
import datetime
from flask import Flask, \
                  render_template, \
                  request, \
                  jsonify

from joblib import load
import category_encoders as ce
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)
# model_app = pickle.load(open("model.pkl", "rb"))
pipeline = load('assets/pipeline.joblib') 

############################################################
# Predict with model
############################################################
def Predictor(list_values):  
    # take one row of feature values
#     X = np.array(list_values).reshape(1,-1)
    columns = ['LATITUDE', 'LONGITUD', 'DAY', 'MONTH', 
               'YEAR', 'DAY_WEEK', 'HOUR', 'FUNC_SYS', 
               'RELJCT1', 'WEATHER', 'ROUTE', 'TWAY_ID', 
               'TWAY_ID2']
    X = pd.DataFrame(list_values, columns=columns)
    y = pipeline.predict(X)
    # convert numpy arrapy to list
    predictions = y.tolist()
    return predictions

############################################################
# index page
############################################################
# @app.route('/')
# @app.route('/index')
# def index():
#     return render_template('index.html')

############################################################
# result page
############################################################
# @app.route('/result', methods=['POST'])
# def result():
#     if request.method == 'POST':
#         data_in = request.form.to_dict()
#         # CAUTION: It is not the same with form element sequence
#         # list_values = list(list_values.values())
#         # {'PetalWidthCm': '1.4', 'SepalWidthCm': '3.5', 
#         #  'SepalLengthCm': '7', 'PetalLengthCm': '4.7'}
#         list_values = [data_in['SepalLengthCm'],
#                        data_in['SepalWidthCm'],
#                        data_in['PetalLengthCm'],
#                        data_in['PetalWidthCm']]        
#         # convert from text to float
#         list_values = list(map(float, list_values))
#         result = IrisPredictor(list_values)  

#     return render_template("result.html", 
#                            prediction=result)

############################################################
# API
############################################################
@app.route("/api", methods=['POST'])  
def api():
    # get input data
    data_in = request.get_json(force=True)
    today = datetime.datetime.today()
    try:
        # parse JSON and transform values to list
        # for prediction:
        # LATITUDE, LONGITUD, DAY, MONTH, YEAR, DAY_WEEK, HOUR,
        # FUNC_SYS, RELJCT1, WEATHER, ROUTE, TWAY_ID, TWAY_ID2, 
        # prediction output:
        # (ACCIDENT) LIKELYHOOD 
        list_values, data_out = [], {}
        for id, values in data_in.items():
            record = [values['LATITUDE'],
                      values['LONGITUD'],
                      today.day, # DAY
                      today.month, # MONTH
                      today.year, # YEAR
                      today.weekday(), # DAY_WEEK
                      today.hour, # HOUR
                      values['FUNC_SYS'],
                      values['RELJCT1'],
                      'NaN', # WEATHER
                      'NaN', # ROUTE
                      values['TWAY_ID'],
                      values['TWAY_ID2'],
                     ]
            list_values.append(record)
            for i, r in enumerate(record):
                if r=="" or r==None:
                    record[i] = 'NaN'
                    
            data_out[id] = {
                'LATITUDE': values['LATITUDE'],
                'LONGITUD': values['LONGITUD'],
                'LIKELYHOOD': 0
                }
            
        # get output data    
        preds = Predictor(list_values)
        for values, pred in zip(data_out.values(), preds):
            print(values, pred)
            values['LIKELYHOOD'] = pred
            
        return data_out
    
    except:
        return jsonify('Invalid parameters!')

if __name__ == '__main__':
    app.run(port=5000, debug=True)