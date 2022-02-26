from crypt import methods
from ctypes import util
from urllib import response
from flask import Flask ,request,jsonify
import util
import sklearn
app = Flask(__name__)

@app.route('/get_location_names',methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations' : util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_price',methods=['POST','GET'])
def predict_home_price():
    print("printing prices")
    avil = request.form['avail']
    fur = request.form['furnish']
    tran = request.form['trans']
    bat = int(request.form['bath'])
    bhk = int(request.form['bedroom'])
    tosqft = float(request.form['sqft'])
    locat = request.form['loc']
    response = jsonify({
        'estimated_price':util.get_estimated_price(tosqft,bat,bhk,avil,fur,tran,locat)
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

if __name__ == '__main__':
    print("Starting python Flask Server For Bhopal House Price Prediction")
    util.load_saved_arfifacts()
    app.run()