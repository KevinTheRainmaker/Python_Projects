import requests
from bs4 import BeautifulSoup

indeed_LIMIT = 50
saramin_LIMIT = 100
indeed_URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={indeed_LIMIT}"
saramin_URL = f"http://www.saramin.co.kr/zf_user/search/recruit?searchType=search&searchword=%ED%8C%8C%EC%9D%B4%EC%8D%AC&recruitPageCount={saramin_LIMIT}"

def extract_pages(URL):
    results = requests.get(URL)
    soup = BeautifulSoup(results.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page

def extract_indeed_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = company_anchor.string
    else:
        company = company.string
    company = company.strip()
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {'title': title, 'company': company, "location": location, "link": f"https://kr.indeed.com/viewjob?jk={job_id}"}

def extract_saramin_job(html):
    title = html.find("h2", {"class": "job_tit"}).find("a")["title"]
    company = html.find("div", {"class": "area_corp"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = company_anchor.string
    else:
        company = company.string
    company = company.strip()
    location = html.find("div", {"class": "job_condition"}).find("a").string
    job_id = html["value"]
    return {'title': title, 'company': company, "location": location, "link": f"http://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx={job_id}"}

def extract_indeed_jobs(last_page):
    jobs = []
    print('Start Scrapping from "INDEED"')
    for page in range(last_page):
        print(f"Scrapping page {page+1}")
        result = requests.get(f"{indeed_URL}&start={page*indeed_LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_indeed_job(result)
            jobs.append(job)
    return jobs

def extract_saramin_jobs(last_page):
    jobs = []
    print('Start Scrapping from "SARAMIN"')
    for page in range(last_page):
        print(f"Scrapping page {page+1}")
        result = requests.get(f"{saramin_URL}&start={page*saramin_LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "item_recruit"})
        for result in results:
            job = extract_saramin_job(result)
            jobs.append(job)
    return jobs

def give_me_job(URL1, URL2):
    last_page_1 = extract_pages(URL1)
    last_page_2 = extract_pages(URL2)

    indeed = extract_indeed_jobs(last_page_1)
    print(indeed)

    saramin = extract_saramin_jobs(last_page_2)
    print(saramin)


#Trial
give_me_job(indeed_URL, saramin_URL)