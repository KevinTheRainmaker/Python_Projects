import requests
from bs4 import BeautifulSoup

indeed_results = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_results.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

links = pagination.find_all('a')

pages = []

for link in links:
    pages.append(link.string) # If Anchor have just one element & element have just one text, it will be same as below
    #pages.append(link.find("span").string) # Only get strings from span

pages = pages[:-1]
print(pages) 