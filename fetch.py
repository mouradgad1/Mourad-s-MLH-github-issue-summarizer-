import requests

def mourad_fetch(x):
    url = f"https://api.github.com/repos/{x}/issues"
    headers = {"Accept": "application/vnd.github.v3+json"}
    z = requests.get(url, headers=headers)
    if z.status_code != 200:
        raise Exception(f"Failed with status code {z.status_code}")
    return [i for i in z.json() if "pull_request" not in i]
