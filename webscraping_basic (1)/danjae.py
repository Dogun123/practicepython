from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time




browser = webdriver.Chrome()
browser.get("https://edu.cbe.go.kr/")

browser.find_element_by_xpath("/html/body/div/div[1]/ul[2]/li[1]/span/a").click()



# time.sleep(1)

# browser.find_element_by_xpath('//*[@id="frm"]/div/label[1]').send_keys("tpdnd7890")