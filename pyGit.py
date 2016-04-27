import requests

# user = raw_input()
# reponame = raw_input()
user = 'zulip'
reponame = 'zulip'
sin = '2016-04-10T00:00:00Z'
unt = '2016-04-20T00:00:00Z' 

path = 'https://api.github.com/users/' + user + '/repos'
new_path = 'https://api.github.com/repos/' + user + '/' + reponame + '/commits?until='+ unt + '&since=' + sin

response = requests.get(path, auth = ('Your Github Username', 'Your Github Password'))
first_response = requests.get(new_path, auth = ('Your Github Username', 'Your Github Password'))
# second_response = requests.get(new_path, headers = headers)

print response
print '=============================================================================='
print first_response
print '=============================================================================='

assert response.status_code == 200
assert first_response.status_code == 200

for repo in response.json():
	print '[{}] {} ========> {}'.format(repo['language'], repo['name'], repo['description'])
	print '=============================================================================='

count = 0

for commit in first_response.json():
   	print '{} {} {}'.format(commit['commit']['committer']['name'], commit['commit']['committer']['date'], commit['sha'])
  	var = commit['sha']
  	# print var
  	test_path = 'https://api.github.com/repos/' + user + '/' + reponame + '/commits/' + var
  	# print test_path
  	commit_values = requests.get(test_path, auth = ('Your Github Username', 'Your Github Password'))
  	# print commit_values
  	comm = commit_values.json()
  	# printkon comm
  	print 'Additions {} Deletions {} Total {}'.format(comm['stats']['additions'], comm['stats']['deletions'], comm['stats']['total'])
  	print '=============================================================================='
  	count += 1

# for commit in first_response.json():
#   	print '{} {} {}'.format(commit['commit']['committer']['name'], commit['commit']['committer']['date'], commit['sha'])
#   	print '=============================================================================='
#   	count += 1
print count