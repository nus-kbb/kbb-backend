import mysql.connector
import json
from flask import Flask
app = Flask(__name__)

@app.route('/home')
def hello_world():
    return 'Serving Hello world!'

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port=3000)