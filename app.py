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
data_file =  open('sample.json')    
data = json.load(data_file)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = "testwebhook"

   
    return res

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
