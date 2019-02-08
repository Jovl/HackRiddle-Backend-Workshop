from flask import Flask, jsonify, request
from firebase import firebase

app = Flask(__name__)
fb = firebase.FirebaseApplication('https://.firebaseio.com/', None)


@app.route('/', methods=['POST'])
def add_user():
    user_data = request.get_json(force=True)
    response = fb.put('/users', user_data['email'], user_data)
    return jsonify(response)


