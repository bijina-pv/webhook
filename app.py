import urllib
import json
import os


from pprint import pprint
from flask import Flask
from flask import request
from flask import make_response
from flask import url_for
from flask import redirect
import sys
import logging

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
data_file =  open('sample.json')    
data = json.load(data_file)

@app.route('/', methods=['GET'])
def root():
	return "Sample webhook to connect to api.ai chatbot."

@app.route('/webhook', methods=['POST'])
def webhook():
   
    res = makeWebhookResult(req)
    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


   
def makeWebhookResult(req):
    speech="hi"
    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-onlinestore-shipping"
    }

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
