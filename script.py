import requests
import os
from git import Repo
import shutil
# you need create a folder named "repos" before run it 
repo_owner = "" # change
repo_name = "" # change

def get_username(commit):
    return commit.author.name

def get_email(commit):
    return commit.author.email

def impersionate(username, email):
    print('username: ' + username, 'email: ' + email)
    os.system("git config --global user.name \"" + username + "\"")
    os.system("git config --global user.email \"" + email + "\"")
    with open("README.md", 'a') as f:
        f.write(' ')
        f.close()
    os.system("git add README.md")
    os.system(f"git commit -m \"{username}\"")

if os.path.lexists(f'./repos/{repo_name}'):
    shutil.rmtree(f'./repos/{repo_name}', ignore_errors=True)

print('Cloning repo...')
Repo.clone_from(f"https://github.com/{repo_owner}/{repo_name}.git", f"./repos/{repo_name}")
print('Cloned repo!')
repo = Repo(f"./repos/{repo_name}")
print('Getting commits...')
commits = list(repo.iter_commits())
users = []
try:
    for commit in commits:
        if not '+' in get_email(commit) and not ' ' in get_username(commit):
            if get_username(commit) not in users:
                users.append(get_username(commit))
                impersionate(get_username(commit), get_email(commit))
            else:
                continue
    os.system('git push')
    shutil.rmtree(f'./repos/{repo_name}', ignore_errors=True)
except KeyboardInterrupt:
    os.system('git push')
    shutil.rmtree(f'./repos/{repo_name}', ignore_errors=True)
