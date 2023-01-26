from bs4 import BeautifulSoup
import requests
import urllib.parse

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass
    
target_url = "http://192.168.75.134/mutillidae/index.php?page=dns-lookup.php"
response = requests(target_url)

parsed_html = BeautifulSoup(response.content.decode(), "html.parser")
forms_list = parsed_html.findAll("form")

for form in forms_list:
    action = form.get("action")
    post_url = urllib.parse.urljoin(target_url, action)
    method = form.get("method")
    
    input_list = parsed_html.find_all("input")
    post_data = {}
    
    for input in input_list:
        input_name = input.get("name")
        input_type = input.get("type")
        input_value = input.get("value")
        
        if input_type == "text":
            input_value = "s7ee7.com"
            
        post_data[input_name] = input_value
    
    result = requests.post(post_url, data=post_data)
    print(result.content.decode())