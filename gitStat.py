import sys
import requests
import json
import threading
# This function is called when the server recieves the request
# with username, repo name, starting date, and ending date.
# Using these parameters it returns
# Name of committer Date of Commit SHA value in a form of
# json data dump.

def getGitStat(username, repo, sinD, untD, response_url):

    user = username
    reponame = repo
    sin = "2016-{}T00:00:00Z".format(sinD)
    unt = "2016-{}T00:00:00Z".format(untD)

    strings = ""
    details = {}
    page = 1
    counter = 0

    user_repo_path = "https://api.github.com/users/{}/repos".format(user)
    first_response = requests.get(
        user_repo_path, auth=(
            'IshanGupta10', 'explosmrob10'))

    assert first_response.status_code == 200

    while(page < 10):

        repo_commits_path = "https://api.github.com/repos/{}/{}/commits?page={}&per_page=100&until={}&since={}".format(
            user, reponame, str(page), unt, sin)
        second_response = requests.get(
            repo_commits_path, auth=(
                'IshanGupta10', 'explosmrob10'))

        assert second_response.status_code == 200

        for commit in second_response.json():

            sha_commits_path = "https://api.github.com/repos/{}/{}/commits/{}".format(
                user, reponame, commit['sha'])
            commit_values = requests.get(
                sha_commits_path, auth=(
                    'IshanGupta10', 'explosmrob10'))

            assert commit_values.status_code == 200

            comm = commit_values.json()

            conv = "{} {} {}".format(commit['commit']['committer']['name'], commit[
                                     'commit']['committer']['date'], commit['sha'])
            
            strings = "{}{}\n".format(strings, conv)

            counter += 1

        page += 1

    # response_url = request.args["response_url"]

    if not strings:
    	strings = "No commits were made between the given date interval"
    
    response_url = response_url

    payload = {
        "response_type": "ephemeral",
        "text": "Github Repo Commits Status",
        "attachments": [
            {
                "text": strings
            }
                ]
        }

    headers = {'Content-Type': 'application/json',
            'User-Agent': 'Mozilla /5.0 (Compatible MSIE 9.0;Windows NT 6.1;WOW64; Trident/5.0)'}

    response = requests.post(response_url, json = payload, headers = headers)
