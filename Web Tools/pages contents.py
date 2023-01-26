import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass
target_url = "s7ee7.com"
response = request (target_url)
print (response.content.decode())