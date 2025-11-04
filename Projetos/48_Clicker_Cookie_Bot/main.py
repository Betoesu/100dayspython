from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep,time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")

sleep(3)

select_language = driver.find_element(By.XPATH,value='//*[@id="langSelect-PT-BR"]')
select_language.click()

sleep(2)

cookie = driver.find_element(By.CSS_SELECTOR,"div button")

#Timers
wait_time = 5
timeout = time() + wait_time


while True:
    cookie.click()
    
    if time() > timeout:
        products = []
        for i in range(19,-1,-1):
            try: #Uso Try para caso nao haja algum product{10 por exemplo} ele continua o código
                prod = driver.find_element(by=By.ID,value=f"product{i}")
                #Verifico se existe a palavra enabled na classe do product
                if "enabled" in prod.get_attribute("class"):
                    products.append(prod)
            except:
                continue

        if products:
            products[-1].click()

        timeout = time() + wait_time 