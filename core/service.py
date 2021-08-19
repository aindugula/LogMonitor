import requests

#get the response from a Rest API service
def getresponse(path):
    return requests.get(path).json()
    
if __name__ == "__main__":
    print(getresponse("http://127.0.0.1:5000/logs"))
