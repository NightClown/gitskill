from flask import json
from flask import Flask
from flask import request

app = Flask(__name__)

# @app.route('/hello')
#
# def api_hello():
#
#     if 'name' in request.args:
#
#         return 'Hello' + request.args['name']
#
#     else:
#
#         return 'Sorry,no name'


@app.route('/messages', methods=['POST'])

def api_message():

    if request.headers['Content-Type'] == 'text/plain':

        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':

        return "JSON Message:" + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':

        f = open('./binary', 'wb')

        f.write(request.data)

        f.close()

        return "Binary message written!"

    else:

        return "415 Unsupported Media Type ;)"

if __name__ == '__main__':

    app.run()

