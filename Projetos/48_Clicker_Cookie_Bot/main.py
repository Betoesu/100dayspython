from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

sleep(3)

select_language = driver.find_element(By.XPATH,value='//*[@id="langSelect-PT-BR"]')
select_language.click()

sleep(2)

available_list = driver.find_elements(By.CSS_SELECTOR, value="div[id='products']")
del available_list[0]
for n in available_list:
    print(n.text)

cookie = driver.find_element(By.CSS_SELECTOR,"div button")
while True:
    cookie.click()
    available_list = driver.find_elements(By.CSS_SELECTOR, value="div[id='products']")
    for n in available_list:
        print(n.text)

    