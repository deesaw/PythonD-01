from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.commin.keys import Keys 
import time
browser = webdriver.Firefox()
browser.get('http://www.google.com')

#element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "gbqfq")))


search = browser.find_element_by_name('q')
search.send_keys("google search through python")
search.send_keys(keys.RETURN)

#browser.find_element_by_css_selector('.jsb > center:nth-child(1) > input:nth-child(1)').click()
#browser.quit()
