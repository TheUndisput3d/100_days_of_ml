from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Prevents the browser from closing

s = Service("C:/Users/Aayush/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=s, options=chrome_options)

driver.get('http://google.com')
# time.sleep(1)

# fetch the search input box using xpath
user_input = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea")
user_input.send_keys('Campusx')
time.sleep(1)

user_input.send_keys(Keys.ENTER)
time.sleep(1)

link = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div[12]/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/div[1]/div/span/a")
link.click()

time.sleep(1)
link2 = driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[2]/a[1]")
link2.click()