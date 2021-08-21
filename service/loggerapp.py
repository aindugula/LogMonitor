from flask import Flask
from flask import json
from flask import jsonify
from flask import request
import sys
sys.path.append('../core/')
import listFilesInDir as filesList
import logContents
import logging

app = Flask(__name__)

#http://127.0.0.1:5000/
@app.route("/")
def Welcome():
    return "Welcome to logger app!"

#http://127.0.0.1:5000/logs
@app.route('/logs', methods=['GET'])
def logs():
    response = filesList.listFilesInDir('/var/log')
    app.logger.info('files request successfull')
    return jsonify(response)
    
#http://127.0.0.1:5000/logs?n=3&search=term
@app.route('/logs/<string:logfile>', methods=['GET'])
def get(logfile):
    path = '/var/log/'
    N = None
    searchTerm = None
    if 'n' in request.args:
        N = int(request.args['n'])
    if 'search' in request.args:
        searchTerm = request.args['search']
    
    response = logContents.logContents_Tail(path + logfile, N, searchTerm)
    
    app.logger.info('log request successfull')
    
    return jsonify(response)

if __name__ == "__main__":
    logging.basicConfig(filename='loggerapp.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')

