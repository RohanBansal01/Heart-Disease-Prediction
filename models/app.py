from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
import cv2
import pickle
import imutils
import sklearn
from tensorflow.keras.models import load_model
# from pushbullet import PushBullet
import joblib
import numpy as np
from tensorflow.keras.applications.vgg16 import preprocess_input


# Loading Models

heart_model = pickle.load(open('models/heart_disease.pickle.dat', "rb"))


# Configuring Flask
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS



########################### Routing Functions ########################################

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/heartdisease')
def heartdisease():
    return render_template('heartdisease.html')

@app.route('/heartform')
def heartform():
    
    return render_template('heartform.html')






########################### Result Functions ########################################





@app.route('/heartform', methods=['POST','GET'])
def heart():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form['gender']
        nmv = float(request.form['nmv'])
        tcp = float(request.form['tcp'])
        eia = float(request.form['eia'])
        thal = float(request.form['thal'])
        op = float(request.form['op'])
        mhra = float(request.form['mhra'])
        age = float(request.form['age'])
       
        print(np.array([nmv, tcp, eia, thal, op, mhra, age]).reshape(1, -1))
        pred = heart_model.predict(
            np.array([nmv, tcp, eia, thal, op, mhra, age]).reshape(1, -1))
        # pb.push_sms(pb.devices[0],str(phone), 'Hello {},\nYour HeartDisease test results are ready.\nRESULT: {}'.format(firstname,['NEGATIVE','POSITIVE'][pred]))
        return render_template('result.html', r=pred)





# No caching at all for API endpoints.



if __name__ == '__main__':
    app.run(debug=True)
