from flask import Flask,request
import requests

from api import getGitStat

import os
app =Flask(__name__)

@app.route('/', methods=['POST','GET'])
def handle_data():
    text= request.args["text"].split("/")
    user = text[0]
    repo = text[1]
    sinD = text[2]
    untD = text[3]
    temp =  getGitStat(user,repo,sinD,untD)
    response_url = request.args["response_url"]
    print response_url
    headers = { "content-type":"application/json"}
    postStatus = requests.post(url=response_url,data=temp,headers=headers)
    print postStatus.status_code
    print temp
    #return "hello"
    return temp


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80,debug=True)
