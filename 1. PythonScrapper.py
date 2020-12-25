import requests
from bs4 import BeautifulSoup

indeed_results = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_results.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

links = pagination.find_all('a')

pages = []

for link in links[:-1]:
    pages.append(int(link.string)) 
    #int() => to integer / TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType' >> 'Cause of 'Next'
    # links[]:-1]

#pages = pages[:-1]
max_page = pages[-1]

#end of url; start = ~~ >> '~~' == (PageNum-1) * limit(in this case, 50) 