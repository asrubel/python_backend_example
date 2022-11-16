from flask import Flask, jsonify
from app.load import load_all_students

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/college/lecture')
def hello_from_college():
    return 'Hello from college!'


@app.route('/college/all_students')
def load_all():
    return jsonify(load_all_students())
