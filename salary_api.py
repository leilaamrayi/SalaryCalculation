from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pandas as pd
import pickle as p
import json

#Create flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Hey Jakob"

@app.route("/salary", methods=["POST"])
def salary_perdict():
    request_json=request.json
    query_df=pd.DataFrame(request_json)
    print("query_df is:")
    print(query_df.head())
    prediction = (model.predict(query_df))
    print(prediction)
    prediction_value=prediction[0]
    response={'result':str(prediction_value)}
    print("response is:")
    print(response)
    return json.dumps(response)

# comment out the following code block to disable REST API
if __name__ == '__main__':
    model_file = 'model_prediction.pickle'
    model = p.load(open(model_file, 'rb'))
    app.run(debug=True)



# uncomment the following code block for local test without REST API
# if __name__ == '__main__':
#     model_file = 'model_prediction.pickle'
#     model = p.load(open(model_file, 'rb'))
#     request_text = open("request.json", "r")
#     request_json = json.load(request_text)
#     query_df=pd.DataFrame(request_json)
#     print("query_df is:")
#     print(query_df.head())
#     prediction = (model.predict(query_df))
#     print(prediction)

