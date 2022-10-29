import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle


app=Flask(__name__)
model=pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # int_features = [int(x) for x in request.form.values()]
    # final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)


    int_features = []
    for x in request.form.values():
        int_features.append(x)

    print(int_features)    

    if (int_features[0].lower())=='sunny':
        int_features[0]=1
    elif (int_features[0].lower())=='rain':
        int_features[0]=0

    if (int_features[1].lower())=='high':
        int_features[1]=0
    elif (int_features[1].lower())=='normal':
        int_features[1]=1

    if (int_features[2].lower())=='strong':
        int_features[2]=0
    elif (int_features[2].lower())=='weak':
        int_features[2]=1

    print(int_features)                  

    final_features=[int_features]




    output = model.predict(final_features) #'play' #round(prediction[0], 2)

    if int(output[0])==0:
        result='will not play'
    elif int(output[0]==1):
        result='will play'    


    return render_template('index.html', prediction_text='Today the person  {}'.format(result))


if __name__ == "__main__":
    app.run(debug=True)    
