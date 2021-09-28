# Welcome to Kangbeen's Python Playground

## Project 1. PythonScrapper (last updated: 2021-04-23)
**Overview:**
Get job informations from two sites(in here, 'Indeed' & 'Saramin') and save them in Excel file. After saving is done, you can receive it with your Email automatically.

## You can see more cool project using this at the <a href = 'https://github.com/KevinTheRainmaker/BugBug'>BugBug</a> Repository 
</br>

### **Error Type**</br>

- **smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted.:**</br>
You must have entered the wrong email address or the wrong password. </br>
If not, set 'Allow low-security apps to access your account' in your sender Email setting.
</br></br>

- **smtplib.SMTPAuthenticationError: (534, b'5.7.9 Application-specific password required.:**</br>
These messages often appear when 2-Step-Verification is enabled.</br>
Click the URL of the error message to release the 2nd stage of authentication.
</br></br>

- **PermissionError: [Errno 13] Permission denied:**</br>
There are several reasons for this error. The cases are below.
    - Wrong file path 
    - Unspecified file name 
    - Unspecified file format 
    - Not using \\ or / as the directory delimiter 
    - Too many files 
    - The file is in use by a program other than the development environment
</br></br>

---
</br>

## Project 2. Card Games - Rainbow Holdum
**Overview**
A project to implement various types of card games in Python and calculate the probability of each case after playing countless games.

<br/>

### ***Game #1: Rainbow Holdum***

<br/>

**0. 게임 준비**

    'A' 카드 1장, '2' 카드 2장 ~ '9' 카드 9장, '10' 카드 10장, 총 1에서 10까지 55장의 카드가 필요.

**1. 게임 시작**
    
    딜러는 참가자들에게 카드를 3장씩 나누어준 뒤, 커뮤니티 카드 4장을 중앙에 배치한다.

    플레이어들은 핸드 세 장 상태에서 베팅이 가능하며, 베팅의 순서는 공개된 카드 중에서 가장 숫자가 작은 사람부터 하게 된다.

    아무도 베팅을 하지 않거나(체크), 모든 플레이어가 콜/폴드(다이)를 했다면 커뮤니티 카드 1장을 공개하고 베팅 라운드로 들어간다.

    이후부터는 커뮤니티 카드가 공개될 때마다 베팅이 이루어진다. (총 4번)

    베팅의 순서는 공개된 카드 중에서 가장 숫자가 작은 사람부터 하게 된다. 

    즉, 커뮤니티 카드 오픈 시 선 플레이어가 바뀔 수 있다.
    ( 만약 올인이라면 카드 오픈까지 추가 베팅을 하지 않아도 된다.)

    테이블 중앙(혹은 딜러 자리)에 4장의 카드가 모두 공개되면, 즉 자신의 카드 3장과 커뮤니티 카드 4장, 총 7장이 되었다면 마지막 베팅을 하고 승패를 확정한다. 

**2. 점수 계산**

    자신의 카드와 공개된 카드 7장 중에서, 숫자가 겹치는 카드는 모두 총합에서 제외된다.

    제외된 카드를 뺀 나머지 카드의 총 합이 낮은 사람이 승리하게 되는데 만약 7장의 카드가 모두 서로 다른 숫자라면 '레인보우 홀덤'이 되어 승리.
    (같은 레인보우 홀덤일 경우, 무승부)

**3. 구현**

    위 게임 룰에 따라 게임을 구현하고, 이 중 '레인보우 홀덤'의 확률을 계산해보자.
    게임은 총 1,000,000번 진행되며, 모든 카드는 랜덤으로 배분된다.

**4. 결과**

    수행 결과, 약 4%의 확률로 '레인보우 홀덤'이 나와 승리할 수 있음을 알 수 있다.
    이는 수학적으로도 계산할 수 있다.
</br></br>

---
</br>

## Project 3. Automated Script for Temperature Check
</br></br>

---
</br>

## Project 4. Lotto Program Usin Pseudo random number generator (LCG)
</br></br>