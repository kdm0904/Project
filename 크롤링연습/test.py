from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
# 명시적 대기를 위해 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

main_url = 'http://veneco.kr/'

driver = wd.Chrome(executable_path='chromedriver.exe')
driver.get(main_url)
driver.find_element_by_xpath('//*[@id="gnb_1dul"]/li[8]/a').click()
