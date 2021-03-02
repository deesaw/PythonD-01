from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get('http://www.mongofactory.com')

element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "mce-EMAIL")))
print("Element located")
name=browser.find_element_by_css_selector('.your-name > input:nth-child(1)')
name.send_keys(Keys.NULL)
name.send_keys("Ramesh Sannareddy")

email=browser.find_element_by_css_selector('.wpcf7-email')
email.send_keys("ramesh@mongofactory.com")

subject=browser.find_element_by_css_selector('.your-subject > input:nth-child(1)')
subject.send_keys("Selenium Testing")

mesg=browser.find_element_by_css_selector('textarea.wpcf7-form-control')
mesg.send_keys("Thank you for allowing to use your site for selenium testing")

submit=browser.find_element_by_css_selector('.wpcf7-submit')
submit.click()

browser.find_element_by_css_selector('.jsb > center:nth-child(1) > input:nth-child(1)').click()
#browser.quit()

