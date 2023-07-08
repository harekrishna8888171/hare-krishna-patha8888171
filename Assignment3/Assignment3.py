# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://github.com/")
time.sleep(4)


git_click = driver.find_element("xpath", "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div/a")
git_click.click()
time.sleep(4)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
git_email = driver.find_element("id", "login_field")
git_email.send_keys("harekrishna8888171")
time.sleep(4)

git_pwd = driver.find_element("id","password")
git_pwd.send_keys("Srilakshmi.161991@gmail.com")
time.sleep(4)

git_signin = driver.find_element("xpath", "/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[13]")
git_signin.click()
time.sleep(4)

search_click = driver.find_element("xpath", "/html/body/div[1]/div[1]/header/div/div[2]/div[1]/qbsearch-input/div[1]/div[1]/div/div/button/div")
search_click.click()
time.sleep(4)

search_bar = driver.find_element("xpath","/html/body/div[1]/div[1]/header/div/div[2]/div[1]/qbsearch-input/div[1]/div[2]/modal-dialog/div/div/div/form/query-builder/div[1]/div[1]/div/div[2]/input")
search_bar.send_keys("Conestoga")
search_bar.send_keys(Keys.RETURN)
time.sleep(4)
# assert "Conestoga" in driver.title
# time.sleep(4)

# Closing the webdriver
driver.close()
