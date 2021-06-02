from selenium import webdriver
import time
#Need python installed i used Python 3.9.5
#Need selenium python package installed i used selenium 3.141.0
#Need chrome web browser installed 
#Need chrome web driver executable at this location: "C:\Program Files (x86)\chromedriver.exe"
#Change num to equal now many times you want to click
num = 10
#Run "python test-click.py"
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://interactive.dmagazine.com/competitors/mojo-2/")


for _ in range(num):
    link = driver.find_element_by_link_text("VOTE NOW")
    time.sleep(1)
    link.click()
    
driver.quit()

#if needed import these and add wait statement

# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

