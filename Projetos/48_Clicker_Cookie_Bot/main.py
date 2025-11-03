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

        products = driver.find_elements(By.CSS_SELECTOR,value="div[id^='product']") #Procuro todos os produtos 
        

        best_item = None
        for product  in reversed(products): #Coloco os produtos de forma reversa, ou seja do mais caro para o mais barato

            #Verifico se existe a palavra enabled na classe do product

            if "enabled" in product.get_attribute("class"):
                best_item = product
                break
        
