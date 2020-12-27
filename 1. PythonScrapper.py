import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}"


def extract_indeed_pages():
    results = requests.get(URL)

    soup = BeautifulSoup(results.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]

    return max_page
    # for n in range(max_page):
    #     print(INDEED_URL +"&"+ f"start={n*50}")


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"})
        for result in results:
            title = result.find("h2",{"class":"title"}).find("a")["title"]
            company = result.find("span", {"class":"company"})
            company_anchor = company.find("a")
            if company_anchor is not None:
                company = company_anchor.string
            else:
                company = company.string
            company = company.strip()
            print(title , company)
    return jobs
   
last_page = extract_indeed_pages()
#print(last_page)
extract_indeed_jobs(last_page)