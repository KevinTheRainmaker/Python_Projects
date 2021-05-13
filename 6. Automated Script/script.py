import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

import requests

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2037120074375-2048826409029-DCYN4SugUnl8Ru0vl1uvFv2p"

time.sleep(random.randrange(1,9)*60)

driver = webdriver.Chrome("C:/Users/kgbko1117/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://zeus.gist.ac.kr/sys/main/main.do")
elem = driver.find_element_by_name("login_id") 
elem.send_keys('kgbko1117') 
elem = driver.find_element_by_name("login_pw") 
elem.send_keys('rhrkdqls123!')
elem.send_keys(Keys.ENTER)

try:
    # 찾고자 하는 요소가 iframe 안에 있어 NotFound Error가 발생
    # 이를 해결하기 위해 'driver.switchTo (). frame ()'명령을 사용하여 iframe으로 전환 후 요소 탐색 진행
    element = driver.find_element_by_xpath("//div[@id='ifm_idx_wrap']/iframe")
    driver.switch_to_frame(element)

    page = driver.find_element_by_xpath('//div[@id="mainframe_VFrameSet_HFrameSet_leftFrame_form_gridMenu_body_gridrow_7_cell_7_0_controltreeTextBoxElement"]')
    page.click()
    tab = driver.find_element_by_xpath('//*[@id="mainframe_VFrameSet_HFrameSet_leftFrame_form_gridMenu_body_gridrow_12_cell_12_0_controltreeTextBoxElement"]/div')
    tab.click()

    # input 창을 먼저 클릭해야 해댱 element가 interactable 해지는 구조였기에 발생한 오류
    temp = driver.find_element_by_xpath('//*[@id="mainframe_VFrameSet_HFrameSet_MDIFrameSet_ctxFrameSet_ctxFrame_PERS07^PERS07_08^005^AmcDailyTempRegE_form_div_sample_divMain_divForm_edtTemp_input"]')
    temp.click()
    temp.send_keys('36.'+str(random.randrange(2,8))) 

    save = driver.find_element_by_xpath('//*[@id="mainframe_VFrameSet_HFrameSet_MDIFrameSet_ctxFrameSet_ctxFrame_PERS07^PERS07_08^005^AmcDailyTempRegE_form_div_sample_divMain_btnSave"]').click()

    # UnexpectedAlertPresentException: 예기치않은 팝업창 대처 -> Alert import 하여 accept
    da = Alert(driver)
    da.accept()

    time.sleep(1)
except:
    post_message(myToken,"#bot","체온측정 확인 필요")
    time.sleep(1)
         