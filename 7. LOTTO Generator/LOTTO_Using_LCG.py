import requests
from bs4 import BeautifulSoup

url = 'https://www.dhlottery.co.kr/gameResult.do?method=byWin&wiselog=H_C_1_1'

def extract_winNums(URL):
    global ranNum
    results = requests.get(URL)
    soup = BeautifulSoup(results.text, "html.parser")
    winNums = soup.find("div", {"class": "num win"})
    links = winNums.find_all('span')

    nums = []
    for link in links:
        nums.append(int(link.string))
    # print(nums)
    
    return nums

def get_lotto(seed,m,a,c):
    numSet = []
    num = seed

    for i in range(14):
        num = (a*num + c)%m
        if num != 0:
            numSet.append(int(num))

    numSetEven = sorted(set(numSet))[0::2] # 홀수 인덱스 값(0,2,4,6,8,10..)만 출력
    numSetOdd = sorted(set(numSet))[1::2] # 홀수 인덱스 값(1,3,5,7,9,11..)만 출력
    
    numSetEven = numSetEven[:6]
    numSetOdd = numSetOdd[:6]

    print(numSetEven)
    print(numSetOdd)

    return 0
    
def main():

    global url

    ranNum = 0
    
    while True:
        ranNum = int(input('Choose your seed number(1~45): '))
        if ranNum < 1 or ranNum > 45:
            print("\nError: the number must be from 1 to 45. Please try again.\n")
        else:
            break

    nums = extract_winNums(url)
    
    m = nums[5]
    a = nums[2]

    cIdx = (45%ranNum)%6

    if cIdx == 5:
        c = (a+m)/2
    else:
        c = nums[cIdx]

    # print(m, a, c)
    print('')

    candidates = [m,46,(m+46)//2]
    for candidate in candidates:
        get_lotto(ranNum,candidate,a,c)

    print('\nGood Luck!\n')
    return 0

main()