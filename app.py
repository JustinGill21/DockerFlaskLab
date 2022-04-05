from flask import Flask, jsonify, request, json
import requests
from werkzeug.exceptions import HTTPException
import logging

# As specified in the docker-compose.yml file, FLASK_ENV was set to development
# So, we need to disable the app's Debug environment variable
# Reference: https://flask.palletsprojects.com/en/2.1.x/config/

#DEBUG = False


app = Flask(__name__)
app.config.from_object(__name__)

'''
App Requirements:
1.  All routes must return JSON
2.  All routes must have a docstring

To make custom requests testing the Flask JSON API routes, run the make-request.py script
'''


@app.route('/')
def hello_world():
    ''' No Specified Route '''
    return jsonify('Flask Docker Container says: Hello World!')


@app.route('/ping', methods=['GET'])
def ping_pong():
    ''' ping -> pong '''
    return jsonify('pong!')


@app.route('/word', methods=['GET'])
def random_word():
    ''' fetch a random word, reverse the word, return as json '''

    r = requests.get("https://random-word-api.herokuapp.com/word?number=1")
    object = r.json()[0]
    return jsonify(object[::-1])

@app.route('/string-count', methods=['POST'])
def string_count():
    '''
    Expects a string to be posted, returns the length of the string
    '''
    response_object = {'status':'success'}
    if request.method == 'POST':
        x = request.get_json()
        for key, item in x.items():
            if key != 'status':
                myString = item
        response_object['length'] = str(len(myString))
    return jsonify(response_object)

# Error handling code supplied in lab: https://classes.daveeargle.com/security-analytics-assignments/labs/lab-flask-docker-json-api.html
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    logging.exception(e) # <-- added
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

if __name__ == '__main__':
    app.run()
