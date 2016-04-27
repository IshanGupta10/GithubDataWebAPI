import sys
import requests
import json
from collections import OrderedDict

# This function is called when the server recieves the request
# with username, repo name, starting date, and ending date.
# Using these parameters it returns
# Name of committer Date of Commit SHA value in a form of
# json data dump.


def getGitStat(username, repo, sinD, untD):
    
    user = username
    reponame = repo
    sin = "2016-" + sinD + 'T00:00:00Z'
    unt = "2016-" + untD + 'T00:00:00Z'

    data = {'results': []}
    page = 1
    counter = 0

    user_repo_path = 'https://api.github.com/users/' + user + '/repos'
    first_response = requests.get(
        user_repo_path, auth=(
            'Your Github Username', 'Your Github Password'))

    assert first_response.status_code == 200

    while(page < 10):

        repo_commits_path = 'https://api.github.com/repos/' + user + '/' + reponame + \
            '/commits?page=' + str(page) + '&per_page=100&until=' + unt + '&since=' + sin
        second_response = requests.get(
            repo_commits_path, auth=(
                'Your Github Username', 'Your Github Password'))

        assert second_response.status_code == 200

        for commit in second_response.json():

            sha_commits_path = 'https://api.github.com/repos/' + user + \
                '/' + reponame + '/commits/' + commit['sha']
            commit_values = requests.get(
                sha_commits_path, auth=(
                    'Your Github Username', 'Your Github Password'))

            assert commit_values.status_code == 200

            comm = commit_values.json()

            conv = str(commit['commit']['committer']['name']) + ' ' + \
                str(commit['commit']['committer']['date']) + ' ' + str(commit['sha'])
            data['results'].append(conv)

            counter += 1

        page += 1

    return json.dumps(data)
