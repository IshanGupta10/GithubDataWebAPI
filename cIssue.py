import sys
import requests
import json


def createIssue(username, reponame, token, string):
    user = username
    repo = reponame

    params = string.split(" ")

    data = {
        "title": params[0],
        "body": params[1],
        "assignee": params[2],
        "milestones": params[3],
        "labels": [
            params[4]
        ]
    }

    auth = token

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla /5.0 (Compatible MSIE 9.0;Windows NT 6.1;WOW64; Trident/5.0)',
        'Authorization': 'token %s' % auth}

    create_issue_path = 'https://api.github.com/repos/{}/{}/issues'.format(
        user, repo)

    issue_response = requests.post(
        create_issue_path, json=data, headers=headers)

    issue_values = issue_response.json()

    if second_response.status_code == 201:
        return "Issue created successfully! Issue Number is {}".format(issue_values["number"])
    else:
        return "Please check the data you sent!"
