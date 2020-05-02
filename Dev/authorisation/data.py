import requests



def Code(user):
    payload = {}
    headers = {}
    url = "https://api.github.com/users/" + user
    response = requests.request("GET", url, headers=headers, data = payload)
    print(response)