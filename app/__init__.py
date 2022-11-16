from flask import Flask, jsonify
from app.load import load_all_students
from app.db_init import init

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello students!'


@app.route('/college/lecture')
def hello_from_college():
    return 'Hello from college!'


@app.route('/college/json')
def load_json():
    return jsonify({"university": "KhAI", "college": "IT college", "course": "DevOps"})


@app.route('/college/init_db')
def init_db():
    init()
    return 'DB initialized!'


@app.route('/college/all_students')
def load_all():
    return jsonify(load_all_students())


@app.route('/college/html')
def load_html():
    return """
        <!DOCTYPE html>
        <html>
        <head>
        <title>IT College: DevOps course</title>
        <style>
            body {
                width: 35em;
                margin: 0 auto;
                font-family: Tahoma, Verdana, Arial, sans-serif;
            }
        </style>
        </head>
        <body>
        <h1>IT College: DevOps course</h1>
        <p>This is just example</p>
        </body>
        </html>        
        """
