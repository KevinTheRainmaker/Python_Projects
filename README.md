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

### ***게임 규칙 / Game Rule***

<br/>

>**게임 준비 / Preparation for the Game**

    'A' 카드 1장, '2' 카드 2장 ~ '9' 카드 9장, '10' 카드 10장, 총 55장의 카드가 필요.

    One "A" card, two "2" cards, ..., nine "9" cards, ten "10" cards, hence 55 cards are needed.

<br/>

>**게임 시작 / Game Start**
    
    딜러는 참가자들에게 카드를 3장씩 나누어준 뒤, 커뮤니티 카드 4장을 중앙에 배치한다.
    The dealer distributes three cards to the participants and then places four community cards in the center.

    딜러와 플레이어는 모두 자신의 카드를 한 장씩 공개한다. 이때 플레이어들은 자신의 카드를 확인하여 베팅이 가능하며, 베팅의 순서는 공개된 카드 중에서 가장 숫자가 작은 사람부터 하게 된다.
    The dealer and players all disclose one of their cards. At this time, players can check their cards and bet, and the order of betting is from the person with the smallest number among the disclosed cards.

    플레이어는 베팅을 할 수도, 그냥 포기(다이)를 할 수도 있다. 이렇게 전체 플레이어에 대해 참여 의사 확인이 끝이 나면 딜러는 두 번째 카드를 오픈한다.
    The player can bet or just give up (die). After confirming the intention to participate of the entire player, the round ends, and the dealer opens the second card.

    위 과정을 반복하며, 모든 커뮤니티 카드가 공개될 때까지 진행한다. 이전 라운드에서 포기를 했던 플레이어는 베팅에 참여할 수 없으며, 베팅을 진행했던 플레이어는 이전 라운드에서 자신이 베팅했던 금액과 같거나 높은 금액만을 베팅할 수 있다. 도중에 베팅을 포기하게 될 경우, 이미 베팅된 칩은 회수되지 않는다.
    Repeat the above process and proceed until all community cards are released. Players who gave up in the previous round cannot participate in the bet, and players who made the bet can bet only the same or a higher amount as they bet in the previous round. If the player gives up betting on the way, the chips that have already been bet will not be retrieved.

    (만약 올인이라면 게임 종료 시까지 추가 베팅을 하지 않아도 된다.)
    (If it's all-in, that player don't have to make additional bets until the end.)

    4장의 커뮤니티 카드가 모두 공개되면 게임이 종료된다.
    The game ends when all community cards are released.

<br/>

**2. 점수 계산 / Scoring**

    모든 참가자는 자신의 카드를 공개하고 중앙의 커뮤니티 카드의 숫자와 자신의 카드의 숫자를 합산한다. 이때 숫자가 겹치는 카드는 모두 총합에서 제외된다.
    All participants disclose their cards and add up the number of central community cards with their cards. At this time, all cards with overlapping numbers are excluded from the total.

    카드 숫자의 총 합이 낮은 사람이 승리하게 되는데 만약 7장의 카드가 모두 서로 다른 숫자라면 '레인보우 홀덤'이 되어 승리.
    The person with a low total number of cards wins. However, if all seven cards are different numbers, it becomes a "Rainbow Holdum" and wins.

<br/>

**3. 구현 / Development implementation**

    위 게임 룰에 따라 게임을 구현하고, 이 중 '레인보우 홀덤'의 확률을 계산해보자.
    게임은 총 1,000,000번 진행되며, 모든 카드는 랜덤으로 배분된다.
    Let's implement the game according to the above game rules and calculate the probability of 'Rainbow Holdum'.
    The game will be played a total of 1,000,000 times, and all cards will be distributed randomly.

<br/>

**4. 결과**

    수행 결과, 약 4%의 확률로 '레인보우 홀덤'이 나와 승리할 수 있음을 알 수 있다.
    이는 수학적으로도 계산할 수 있다.
    As a result of the performance, it can be seen that 'Rainbow Holdum' has a probability of about 4%.
    It can also be calculated mathematically.
    
</br></br>

---
</br>

## Project 3. Automated Script for Temperature Check
</br></br>

---
</br>

## Project 4. Lotto Program Usin Pseudo random number generator (LCG)
</br></br>