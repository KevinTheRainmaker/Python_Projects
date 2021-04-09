from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/kgbko/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://zeus.gist.ac.kr/sys/main/main.do")
elem = driver.find_element_by_name("login_id") 
elem.send_keys('kgbko1117') 
elem = driver.find_element_by_name("login_pw") 
elem.send_keys('rhrkdqls123!')
elem.send_keys(Keys.ENTER)

page = driver.find_element_by_xpath('//*[@id="mainframe_VFrameSet_HFrameSet_leftFrame_form_gridMenu_body_gridrow_7_cell_7_0_controltreeTextBoxElement"]')
# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id="mainframe_VFrameSet_HFrameSet_leftFrame_form_gridMenu_body_gridrow_7_cell_7_0_controltreeTextBoxElement"]"}
page.click()

tab = driver.find_element_by_xpath('//*[@id="mainframe_VFrameSet_HFrameSet_leftFrame_form_gridMenu_body_gridrow_12_cell_12_0_controltreeTextBoxElement"]/div')
tab.click()
# elem = driver.find_element_by_id("mainframe_VFrameSet_HFrameSet_MDIFrameSet_ctxFrameSet_ctxFrame_PERS07^PERS07_08^005^AmcDailyTempRegE_form_div_sample_divMain_divForm_edtTemp_input")
# elem.send_keys('36.3')

