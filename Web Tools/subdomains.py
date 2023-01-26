import requests

def request(url):
    try:
        get_response = requests.get("http://" + url)
        print(get_response)
    except requests.exceptions.ConnectionError:
        pass
  
target_url = "google.com"
    
with open ("/home/kali/Desktop/subdomains.txt") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("Discovered subdomain --> " + test_url)
    
requests("google.com")