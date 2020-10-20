import selenium
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://youtube.com')
while True:
    pagetype = driver.find_element_by_xpath('//*[@id="guide"]')
    time.sleep(5)
    print(pagetype)
