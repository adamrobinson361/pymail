from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
from time import sleep
from pandas import DataFrame

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(options=options)

driver.get("https://www.hotukdeals.com")
assert "hotukdeals" in driver.title

# Get scroll height

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

elem = driver.find_elements_by_class_name("cept-tt")

titles = []

for e in elem:
      titles.append(e.get_attribute("Title"))

df = DataFrame(titles, columns=['Title'])

df.to_csv("tmp.csv", index = False)

driver.close()