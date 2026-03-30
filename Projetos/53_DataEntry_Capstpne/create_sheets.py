from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


def create_sheets(forms_link):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(forms_link)

    time.sleep(1)

    responses_button = driver.find_element(By.XPATH,'//*[@id="tJHJj"]/div[3]/div[1]/div/div[2]/span')
    responses_button.click()

    time.sleep(3)

    google_sheet_button = driver.find_element(By.XPATH, '//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/span')
    google_sheet_button.click()