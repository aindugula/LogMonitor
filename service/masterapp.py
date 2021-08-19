from flask import Flask
from flask import json
from flask import jsonify
from flask import request
import sys
sys.path.append('../core/')
from service import getresponse
import logging

#Machine list. This is hard coded here but it can be read from a configuration file
machinedict = {
  "machine01": "127.0.0.1",
  "machine02": "127.0.0.1"
}

app = Flask(__name__)

@app.route("/")
def Welcome():
    return "Welcome to master app!"

@app.route('/machines', methods=['GET'])
def machines():
    response = machinedict
    app.logger.info('machines request successfull')
    return jsonify(response)
    
@app.route('/machines/<string:machinename>', methods = ['GET'])
def getmachine(machinename):
    ip = machinedict[machinename]
    path = "http://"+ip+":5000"+ "/logs"
    return jsonify(getresponse(path))

@app.route('/machines/<string:machinename>/<string:logfile>', methods = ['GET'])
def getlog(machinename, logfile):
    ip = machinedict[machinename]
    path = "http://"+ip+":5000"+ "/logs/" + logfile + "?"
    if 'n' in request.args:
        path = path + "n="+ request.args['n'] + "&"
    if 'search' in request.args:
        path = path + "search=" + request.args['search']
    return jsonify(getresponse(path))

    
#using a different port to test on the same machine
if __name__ == "__main__":
    logging.basicConfig(filename='masterapp.log', level=logging.DEBUG)
    app.run(host='0.0.0.0', port=5001)

