from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://orteil.dashnet.org/cookieclicker/")

#vänta 5 sec innan nästa rad kåd
driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

cursorCounter = 0
    

actions = ActionChains(driver)


def cursor():
    clicker = driver.find_element_by_id("upgrade0")
    upgrade_actions = ActionChains(driver)
    upgrade_actions.move_to_element(clicker)
    upgrade_actions.click()
    upgrade_actions.perform()

while True:
    actions.click(cookie)
    actions.perform()
    #delar på stringen och gör den till en int
    count = int(cookie_count.text.split(" ")[0])
    
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
            cursorCounter+=1
    

    if(cursorCounter > 0) and (count > 100):  
       cursor()
       print("hej")




    