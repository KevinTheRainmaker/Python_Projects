import requests
from bs4 import BeautifulSoup

indeed_results = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_results.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

pages = pagination.find_all('a')

spans = []

for page in pages:
    spans.append(page.find("span"))

spans = spans[:-1]
print(spans) 