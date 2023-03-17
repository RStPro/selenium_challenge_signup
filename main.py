# we need to install python-dotenv
from dotenv import load_dotenv
# we need to install Path
from pathlib import Path
# we need to import os
import os
import time
# we need to install selenium
from selenium import webdriver
# we need to install webdriver-manager to get Service
from selenium.webdriver.chrome.service import Service
# we also need to import By
from selenium.webdriver.common.by import By
# to be able to access the selenium constants we need to import Keys
from selenium.webdriver.common.keys import Keys

# evn path and variables
dotenv_path = Path('Info/.env')
load_dotenv(dotenv_path=dotenv_path)

CHROME_PATH = os.getenv("CHROME_PATH")

#add service
service = Service(executable_path=CHROME_PATH)
driver = webdriver.Chrome(service=service)

URL = "https://en.wikipedia.org/wiki/Main_Page"

#getting site
driver.get(URL)