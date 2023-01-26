import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass
  
target_url = "192.168.100.5/mutillisae/"
    
with open ("/home/kali/Desktop/subdomains.txt") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("Discovered subdomain --> " + test_url)
    
requests(target_url)