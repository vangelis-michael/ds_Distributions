"""Filename: server.py
"""

import os
import pandas as pd
#from sklearn.externals import joblib
import joblib
import dill as pickle
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def apicall():
    """API Call
    
    Pandas dataframe (sent as a payload) from API Call
    """
    path = '/home/michael/Documents/Programming#/Learning APIs/'
    try:
        test_json = request.get_json()
        test = pd.read_json(test_json, orient='records')
        
        # To resolve the issue of TypeError: Cannot compare types 'ndarray(dtype=int64)' and 'str'
        test['Dependents'] = [str(x) for x in list(test['Dependents'])]
    
        # Getting the Loan_IDs seperated out
        loan_ids = test['Loan_ID']
    except Exception as e:
        raise e
        
    clf ='model_v1.pk'
    
    if test.empty:
        return(bad_request())
    else:
        # Load the saved model 
        print("Loading the model...")
	
        loaded_model = None
        with open(path+'models/'+clf, 'rb') as f:
            loaded_model = pickle.load(f)
            
            
        print('The model has been loaded... doing predictions now...')
        predictions = loaded_model.predict(test)
        
        """Add the predictions as Series to a new pandas Dataframe
        
        
                                OR
                                
        
        But we need to send the response codes as well
        """
        responses = jsonify(predictions = final_predictions.to_json(orient='records'))
        
        responses.status_code = 200
        
        return (responses)
    
