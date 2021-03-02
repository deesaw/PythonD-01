from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

browser = webdriver.Firefox()
browser.get('http://www.google.com')


search = browser.find_element_by_name('q')
search.send_keys("the oldest civilization on the earth")
#search.send_keys(Keys.RETURN)

button = browser.find_element_by_css_selector('.jsb > center:nth-child(1) > input:nth-child(1)')
button.click()
#browser.quit()
