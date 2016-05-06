import sys
import requests
import json


def closeIssue(username, reponame, number, token, string):
    user = username
    repo = reponame
    number = number
    params = string.split(", ")

    data = {
        "title": params[0],
        "body": params[1],
        "assignee": params[2],
        "milestones": params[3],
        "state": "closed",
        "labels": [
            params[4]
        ]
    }

    auth = token

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla /5.0 (Compatible MSIE 9.0;Windows NT 6.1;WOW64; Trident/5.0)',
        'Authorization': 'token %s' % auth}

    close_issue_path = 'https://api.github.com/repos/{}/{}/issues/{}'.format(
        user, repo, number)

    issue_response = requests.post(
        close_issue_path, json=data, headers=headers)

    if close_response.status_code == 200:
        return "Issue closed successfully!"
    else:
        return "Please check the data you sent!"
