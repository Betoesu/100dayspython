from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Mantem o chrome aberto dps do programa terminar
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

chrome_options.add_argument("--start-maximized") #Deixa em tela cheia, se abrir em janela o html da página vai estar diferente e dar erro

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# community_portal = driver.find_element(By.LINK_TEXT,value="Community portal")
# community_portal.click()

search = driver.find_element(By.NAME,value="search")

search.send_keys("Jesus",Keys.ENTER) 
