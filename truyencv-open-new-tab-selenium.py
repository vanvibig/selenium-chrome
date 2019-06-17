from selenium import webdriver
import time
 
driver = webdriver.Chrome()
# driver.get('https://python.org')



driver.execute_script('''window.open("http://google.com","_blank");''')