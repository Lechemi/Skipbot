import selenium
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#C:\Program Files (x86)\Google\Chrome\Application
# (Path di chrome)
#chrome.exe -remote-debugging-port=2002 --user-data-dir="C:\Users\mikic\Chrome_Test_Profile"
# (Comando per avviare il browser in debugging mode)

chromeDriverPath = r"C:\ProgramData\chocolatey\bin\chromedriver.exe"

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("debuggerAddress", "localhost:2002")
driver = webdriver.Chrome(executable_path=chromeDriverPath, chrome_options=chromeOptions)

while True:
    try: 
        skipButton = driver.find_elements_by_class_name("ytp-ad-skip-button-container")[0]
        ad = True
        # muteButton = driver.find_elements_by_class_name("ytp-volume-area")[0]
        # muteButton.click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "ytp-volume-area"))).click()

        while ad:
            try:
                skipButton.click()
                ad = False 
            except selenium.common.exceptions.ElementNotInteractableException:
                ad = True
        muteButton = driver.find_elements_by_class_name("ytp-volume-area")[0]
        muteButton.click()
    except IndexError:
        pass
    
