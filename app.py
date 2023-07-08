"""
Created on Sat Jul  8 11:04:43 2023

@author: ABHISHEK
"""
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app1 = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app1.route('/')
def Home():
    return render_template('index.html')

@app1.route('/predict', Method = ['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = round(prediction[0], 2)
    
    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))

if __name__ == "__main__":
    app1.run(debug=True)