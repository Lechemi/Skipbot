import selenium
import time
from selenium import webdriver


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
        adDetector = driver.find_elements_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[17]/div/div[2]/span[3]/button")[0]
        ad = True
        print("Ad detected!")
        muteButton = driver.find_elements_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[27]/div[2]/div[1]/span/button")[0]
        muteButton.click()
        while ad:
            try:
                skipButton = driver.find_elements_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[17]/div[2]/div/div/div[2]/span/button")[0]
                skipButton.click()
                muteButton = driver.find_elements_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[31]/div[2]/div[1]/span/button")[0]
                muteButton.click()
                ad = False
            except IndexError:
                try:
                    skipButton = driver.find_elements_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[17]/div/div[3]/div/div[2]/span/button/div")[0]
                    skipButton.click()
                    muteButton = driver.find_elements_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[31]/div[2]/div[1]/span/button")[0]
                    muteButton.click()
                    ad = False
                except IndexError:
                    pass
    except IndexError:
        pass
    


# muteButton = driver.find_elements_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[27]/div[2]/div[1]/span/button")[0]
# muteButton.click()
# skipButton = driver.find_elements_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[17]/div[2]/div/div/div[2]/span/button")[0]
# skipButton.click()
# skipButton = driver.find_elements_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[17]/div/div[3]/div/div[2]/span/button")[0]
# muteButton = driver.find_elements_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[31]/div[2]/div[1]/span/button")[0]
# muteButton.click()
