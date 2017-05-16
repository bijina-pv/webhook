import urllib
import json
import os

from pprint import pprint
from flask import Flask
from flask import request
from flask import make_response
from flask import url_for
from flask import redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
