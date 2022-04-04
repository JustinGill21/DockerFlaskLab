from flask import Flask, jsonify, request
# As specified in the docker-compose.yml file, FLASK_ENV was set to development
# So, we need to disable the app's Debug environment variable
# Reference: https://flask.palletsprojects.com/en/2.1.x/config/

DEBUG = False


app = Flask(__name__)
'''
App Requirements:
1.  All routes must return JSON
2.  All routes must have a docstring

'''




@app.route('/')
def hello_world():
    return jsonify('Flask Docker Container says: Hello World!')

@app.route('/ping', methods=['GET'])
def ping_pong_route():
    return jsonify('pong!')
    
if __name__ == '__main__':
    app.run()
