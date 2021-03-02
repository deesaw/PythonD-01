from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://www.mongofactory.com/apis/formtest.php')

name=browser.find_element_by_id('name_box')
name.send_keys("Ramesh Sannareddy")

city=browser.find_element_by_id('city_box')
city.send_keys("Hyderbad")

submit=browser.find_element_by_id('submit_button')
submit.click()

#browser.quit()

