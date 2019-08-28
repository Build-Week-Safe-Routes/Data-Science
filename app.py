import numpy as np
import category_encoders as ce
from joblib import load
import json
from flask import Flask, render_template, request, \
                  jsonify
import datetime

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
    X = list_values
    y = pipeline.predict(X)
    data_out = []
    for value in list_values:
        data_out.append({
            'LATITUDE': value[0],
            'LOGITUD': value[1],
            'LIKELYHOOD': y[i]
        })
    return jsonify(data_out)

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
    print(data_in)
    today = datetime.datetime.today()
    try:
        # parse JSON and transform values to list
        # LATITUDE, LONGITUD, DAY, MONTH, YEAR, DAY_WEEK, HOUR,
        # FUNC_SYS, RELJCT1, WEATHER, ROUTE, TWAY_ID, TWAY_ID2, #ACCIDENT
        list_values = []
        for datum in data_in:
            value = [datum['LATITUDE'],
                     datum['LONGITUD'],
                     today.day, # DAY
                     today.month, # MONTH
                     today.year, # YEAR
                     today.weekday, # DAY_WEEK
                     today.hour, # HOUR
                     datum['FUNC_SYS'],
                     datum['RELJCT1'],
                     np.nan, # WEATHER
                     np.nan, # ROUTE
                     datum['TWAY_ID'],
                     datum['TWAY_ID2'],
                    ]
        data_out = Predictor(list_values)
        return data_out
    except:
        return 'Invalid parameters!'

if __name__ == '__main__':
    app.run(port=5000, debug=True)