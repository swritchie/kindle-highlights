from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import set_parameters as sp
import time
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(EdgeChromiumDriverManager().install())

driver.get(sp.parameters['url'])
time.sleep(1)
driver.find_element_by_name('email').send_keys(sp.parameters['username'])

element = driver.find_element_by_name('password')
password = input('What is the password?\n')

element.send_keys(password)
element.send_keys(Keys.ENTER)
time.sleep(1)

book = input('What is the book whose highlights you would like to delete?\n')

while True:
    try:
        element = driver.find_element_by_id('kp-notebook-search-input')
        element.send_keys(book)
        element.send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_elements_by_link_text('Options')[0].send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_elements_by_partial_link_text('Delete')[0].send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="deleteHighlight"]/span/input').send_keys(Keys.ENTER)
        time.sleep(1)
        driver.refresh()
    except IndexError:
        break
    except Exception:
        element.clear()
        element.send_keys(book)
        element.send_keys(Keys.ENTER)
        time.sleep(9)
        driver.find_elements_by_link_text('Options')[0].send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_elements_by_partial_link_text('Delete')[0].send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="deleteHighlight"]/span/input').send_keys(Keys.ENTER)
        time.sleep(1)
        driver.refresh()
    
driver.quit()
print('\007')