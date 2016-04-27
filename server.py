from flask import Flask,request
import requests
from api import getGitStat

import os
app =Flask(__name__)

# This method accepts the argumemnts sent in slack command
# and calls getGitStat method in api.py to process the json
# data of the stats for the Github repository within date
# limits provided by the caller.

@app.route('/', methods=['POST','GET'])
def handle_data():

    text= request.args["text"].split(" ")
    user = text[0]
    repo = text[1]
    sinD = text[2]
    untD = text[3]

    temp =  getGitStat(user, repo, sinD, untD)

    print temp
    return temp


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80,debug=True)