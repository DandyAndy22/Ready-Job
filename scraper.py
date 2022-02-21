## importing libraries
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

position = "delete this and write position here"
local = "delete this and write job location here"

##example below: 
## position = "data scientist"
## local = "brazil"

## formating to linkedin model
position = position.replace(' ', "%20")

## Open browser
driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
#Maximizing browser window to avoid hidden elements
driver.set_window_size(1024, 600)
driver.maximize_window()

## Opening jobs webpage
driver.get(f"https://www.linkedin.com/jobs/search/?geoId=103644278&keywords={position}&location={local}")
## waiting load
time.sleep(2)

