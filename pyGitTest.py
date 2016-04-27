import sys
import requests
import json
# def getGitStat(username, repo, sinD, untD):
# user = raw_input()
# reponame = raw_input()
user = 'zulip'
reponame = 'zulip'
sin = '2016-04-10T00:00:00Z'
unt = '2016-04-20T00:00:00Z'

data = {'results': []}
# first_details = []
# sha = []
# total = []
page = 1
counter = 0

user_repo_path = 'https://api.github.com/users/' + user + '/repos'
first_response = requests.get(user_repo_path, auth=('Your Github Username', 'Your Github Password'))

assert first_response.status_code == 200

# print response
# print
# '=============================================================================='

for repo in first_response.json():
    print '[{}] {} ========> {}'.format(repo['language'], repo['name'], repo['description'])
    print '=============================================================================='

while(page < 10):

    repo_commits_path = 'https://api.github.com/repos/' + user + '/' + reponame + \
        '/commits?page=' + str(page) + '&per_page=100&until=' + unt + '&since=' + sin
    second_response = requests.get(
        repo_commits_path, auth=(
            'Your Github Username', 'Your Github Password'))

    assert second_response.status_code == 200

    # print new_response
    # print
    # '=============================================================================='

    for commit in second_response.json():

        details = {}

        print '{} {} {}'.format(commit['commit']['committer']['name'], commit['commit']['committer']['date'], commit['sha'])

        string = str(commit['commit']['committer']['name']) + ' ' + \
            str(commit['commit']['committer']['date']) + ' ' + str(commit['sha'])

        # first_details.append(var)
        # sha.append(str(commit['sha']))

        sha_commits_path = 'https://api.github.com/repos/' + user + \
            '/' + reponame + '/commits/' + commit['sha']
        commit_values = requests.get(
            sha_commits_path, auth=(
                'Your Github Username', 'Your Github Password'))

        assert commit_values.status_code == 200

        comm = commit_values.json()

        # var = str(comm['stats']['additions']) + ' ' + str(comm['stats']['deletions']) + ' ' + str(comm['stats']['total'])

        # total.append(var)

        details['name'] = commit['commit']['committer']['name']
        details['date'] = commit['commit']['committer']['date']
        details['sha'] = commit['sha']
        details['i_val'] = comm['stats']['additions']
        details['d_val'] = comm['stats']['deletions']
        data['results'].append(details)

        print 'Additions {} Deletions {} Total {}'.format(comm['stats']['additions'], comm['stats']['deletions'], comm['stats']['total'])
        print '=============================================================================='
        
        counter += 1

    page += 1

print data

print counter
