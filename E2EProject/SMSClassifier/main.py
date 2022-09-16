#Libraries to create an API
from flask import Flask,request,render_template
from utils import *
from constants import *

#Library to load model
import pickle


#Loading the required pickle files
classifier = pickle.load(open(modelfile, 'rb'))
cv = pickle.load(open(transformfile, 'rb'))

#Initialising flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        processed_msg = processData(message)
        data = [processed_msg]
        transformed_msg = cv.transform(data).toarray()
        my_prediction = classifier.predict(transformed_msg)
        return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
    app.run(debug=True)