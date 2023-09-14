# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:20:56 2022

@author: HP
"""

from flask import Flask, render_template, request
import pickle
import numpy as np

app= Flask(__name__)
svc_model = pickle.load(open('svc_trained_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/predict', methods=['POST'])
def predict():
   
   
   inputs = []
   inputs.append(request.form['age'])
   inputs.append(request.form['gender'])    
   inputs.append(request.form['cp'])
   inputs.append(request.form['Thalach'])
   
   age = request.form['age']
   gender = request.form['gender'] 
   cp = request.form['cp']
   Thalach = request.form['Thalach']
   

   
   
   final_inputs = [np.array(inputs)]
   prediction = svc_model.predict(final_inputs)
    #unseen_feature_vectors = request.form.values()
   
   if prediction[0] == 1:
        categorical_array = "Diseased"
   if prediction[0] == 0:
        categorical_array = "Not Diseased"
    
   result= categorical_array
   if age=="age":
       age ="age"
       
   if gender=="0":
       gender = "Female"
   if gender=="1":
       gender = "Male"
     
   if cp=="0":
       cp = "Zero"
   if cp=="1":
       cp = "One"
   if cp=="2":
       cp = "Two"
   if cp=="3":
       cp = "Three"
       
   if Thalach=="Thalach":
       Thalach="Thalach"
       
   return render_template('Home.html', prediction_text1=result, age1 = age, gender1=gender, cp1=cp, Thalach1=Thalach)



if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
