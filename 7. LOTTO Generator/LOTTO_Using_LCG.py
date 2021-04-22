import requests
from bs4 import BeautifulSoup

url = 'https://www.dhlottery.co.kr/gameResult.do?method=byWin&wiselog=H_C_1_1'

def extract_winNums(URL,seed):
    global ranNum
    results = requests.get(URL)
    soup = BeautifulSoup(results.text, "html.parser")
    winNums = soup.find("div", {"class": "num win"})
    links = winNums.find_all('span')

    nums = []
    for link in links:
        nums.append(int(link.string))
    # print(nums)
    
    return (nums[2],nums[5], nums[(45 % seed) % 6] + 1)

def get_lotto(m):
    ranNum = 0
    while ranNum < 1 or ranNum > 45:
        ranNum = int(input('Choose your seed number(1~45): '))
        if ranNum < 1 or ranNum > 45:
            print("\nError: the number must be from 1 to 45. Please try again.\n")

    (a, m, c) = extract_winNums(url,ranNum)
    if c >= m:
        c -= 2    
    print(m, a, c)

    numSet = []
    
    for i in range(10):
        ranNum = (a*ranNum + c) % m
        if ranNum != 0:
            numSet.append(ranNum)

    numSet = sorted(list(set(numSet))[:6])

    print(numSet)


get_lotto(m)
get_lotto(46)