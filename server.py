from flask import Flask, request
from api import getGitStat
from createIssue import createIssue
from closeIssue import closeIssue

import os
import requests

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

        headers = {"Content-type": "application/json"}
        postStatus = requests.post(
            url=response_url, data=temp, headers=headers)

        print temp
        return temp

    else:
        return "Please enter correct details. Check if the username or reponame exists, and/or Starting date < End date. Also, date format should be MM-DD"


@app.route('/createissue/<token>', methods=['POST', 'GET'])
def create_Issue(token):
    params = request.args["text"].split(" | ")
    value = createIssue(params[0], params[1], token, params[2])
    return value


@app.route('/closeissue/<token>', methods=['POST', 'GET'])
def closee_Issue(token):
    params = request.args["text"].split(" | ")
    value = closeIssue(params[0], params[1], params[2], token, params[3])
    return value


@app.route('/helpgit', methods=['POST', 'GET'])
def help_git():
    value = "****************************************\n \
            Git Commands Helper for Squadrun \n \
            **************************************** \n \
            /get_git : Username Reponame StartDate(MM-DD) EndDate(MM-DD) \n \
            /createissue : Username | Reponame | Title, Body, Assignee, Milestones, Labels    Copy this format and replace the values of your need. \n \
            /closeissue : Username | Reponame | IssueNumber Copy this format and replace the values of your need."
    return value


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
