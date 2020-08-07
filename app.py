# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model1.pkl', 'rb'))

@app.route('/')
def hello():
    return render_template('index.html')
    
@app.route('/predict',methods=['GET','POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if request.method == "POST":
        myDict = request.form
        TotalWorkingYears = int(myDict['workingyears'])
        HourlyRate = int(myDict['hourlyrate'])
        MonthlyRate = int(myDict['monthlyrate'])
        JobRole = int(myDict['jobrole'])
        OverTime = int(myDict['overtime'])
        PercentSalaryHike = int(myDict['percentsalaryhike'])
        YearsWithCurrManager = int(myDict['yearswithcurrmanager'])
       
        int_features = [[TotalWorkingYears,HourlyRate,MonthlyRate,JobRole,OverTime,PercentSalaryHike,YearsWithCurrManager]]
        prediction = model.predict(int_features)
        pred_prob = model.predict_proba(int_features)

    if(prediction == 0):
        return render_template('index.html',output="Congratulations! This Employee will be loyal to Organisation, will not leave the Organisation.\nThe probability of not leaving the Organisation is %.2f"%(pred_prob[0][0]*100)+"%.")
    else:
        return render_template('index.html',output="It is predicted that this Employee will leave the Organisation.\nThe probability of leaving Organisation is %.2f"%(pred_prob[0][1]*100)+"%.")

    
    
if __name__ == "__main__":
    app.run(debug=True)