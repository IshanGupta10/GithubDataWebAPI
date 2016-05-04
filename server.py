from flask import Flask, request
import requests
from api import getGitStat

import os
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def handle_data():
    params = request.args["text"].split(" ")

    user_repo_path = "https://api.github.com/users/{}/repos".format(params[0])
    first_response = requests.get(
        user_repo_path, auth=(
            'Your Github Username', 'Your Github Password'))

    repo_commits_path = "https://api.github.com/repos/{}/{}/commits".format(params[
                                                                            0], params[1])
    second_response = requests.get(
        repo_commits_path, auth=(
            'Your Github Username', 'Your Github Password'))

    if(first_response.status_code == 200 and params[2] < params[3] and second_response.status_code == 200):

        temp = getGitStat(params[0], params[1], params[2], params[3])
        response_url = request.args["response_url"]

        headers = {"content-type": "application/json"}
        postStatus = requests.post(
            url=response_url, data=temp, headers=headers)

        print temp
        return temp

    else:
        return "Please enter correct details. Check if the username or reponame exists, and/or Starting date < End date. Also, date format should be MM-DD"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
