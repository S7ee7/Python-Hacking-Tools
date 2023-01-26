import requests
import re
import urllib.parse
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="target_url", help="Specify URL, -h for help")
    options, argumants = parser.parse_args()
    
    if not options.target_url:
        "[-] Please specify URL, -h for help"
    
    return options.target_url

target_url = get_arguments
target_link = []

def get_link(url):
    response = requests.get(target_url)
    return re.findall('(?:href=")(.*?)"', response.content.decode())

def crawl(url):
    href_link = get_link(url)
    for link in href_link:
        link = urllib.parse.urljoin(url, link)
        
        if "#" in link:
            link = link.split("#")[0]
            
        if url in link not in target_link:
            target_link.append(link)
            print(link)
            crawl(link)

crawl(target_url)
