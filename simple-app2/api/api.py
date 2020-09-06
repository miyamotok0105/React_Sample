import time
from flask import Flask
from flask_cors import CORS,cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/time')
@cross_origin(supports_credentials=True)
def get_current_time():
    return {'time': time.time()}
