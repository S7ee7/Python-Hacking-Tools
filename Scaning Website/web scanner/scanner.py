import requests
import re
import urllib.parse

class Scanner:
    def __init__(self, url, block_links):
        self.session = requests.Session()
        self.target_url = url
        self.target_links = []
        self.avoid_block_links = block_links
    
    def get_link(self, url):
        response = self.session.get(url)
        return re.findall('(?:href=")(.*?)"', str(response.content))

    def crawl(self, url=None):
        
        if url == None:
            url = self.target_url
            
        
        href_link = self.get_link(url)
        for link in href_link:
            link = urllib.parse.urljoin(url, link)
            
            if "#" in link:
                link = link.split("#")[0]
                
            if url in link not in self.target_link and link not in self.avoid_block_links:
                self.target_link.append(link)
                print(link)
                self.crawl(self.target_links)