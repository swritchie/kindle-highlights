from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import set_parameters as sp
import time

driver = webdriver.Safari()

driver.get(sp.parameters['url'])

driver.find_element_by_name('email').send_keys(sp.parameters['password'])
element = driver.find_element_by_name('password')
element.send_keys(sp.parameters['password'])
element.send_keys(Keys.ENTER)

time.sleep(3)

while True:
    element = driver.find_element_by_id('kp-notebook-search-input')
    element.send_keys(sp.parameters['book'])
    element.send_keys(Keys.ENTER)
    time.sleep(3)
    driver.find_elements_by_link_text('Options')[0].send_keys(Keys.ENTER)
    time.sleep(3)
    driver.find_elements_by_partial_link_text('Delete')[0].send_keys(Keys.ENTER)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="deleteHighlight"]/span/input').send_keys(Keys.ENTER)
    time.sleep(3)
    driver.refresh()