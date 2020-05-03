
import requests
import json


def main(token):
    payload = {}
    headers = {
        'Authorization' : 'Token' + token
    }
    url = "https://api.github.com/users/"
    response = requests.request("GET", url, headers=headers, data = payload)
    data = json.loads(response.text)
    repos = get_repos(data['repos_url'], token)
    dicti = {
        'username': data['login'],
        'profile_photo': data['avatar_url'],
        'github_url':data['url'],
        'type':data['type'],
        'name':data['name'],
        'location': data['location'],
        'email' : data['email'],
        'bio': data['bio'],
        'public_repos': data['public_repos'],
        'followers': data['followers'],
        'following': data['following'],
        'repos':repos
        }
    print(dicti)


def get_repos(url,token):
    payload = {}
    headers = {
        'Authorization' : 'Token' + token
    }
    url = "https://api.github.com/users/"
    response = requests.request("GET", url, headers=headers, data = payload)
    data = json.loads(response.text)
    contrib = get_contrib(data['contributors_url'], token)
    mydicti = []
    for i in data:
        dicti = {
            'name' : i['name'],
            'url':i['html_url'],
            'description': i['description'],
            'forks_count':i['forks_count'],
            'open_issues_count': i['open_issues_count'],
            'open_issues':i['open_issues'],
            'forks':i['forks'],
            'watchers':i['watchers'],
            'default_branch':i['default_branch'],
            'contributors': contrib
            }
        mydicti.append(dicti)
    return mydicti


def get_contrib(url,token):
    payload = {}
    headers = {
        'Authorization' : 'Token' + token
    }
    url = "https://api.github.com/users/"
    response = requests.request("GET", url, headers=headers, data = payload)
    data = json.loads(response.text)
    mydicti = []
    for i in data:
        dicti= {
            'username': i['login'],
            'contributions':i['contributions']
             }
        mydicti.append(dicti)
    return mydicti




main("<TOKEN>")