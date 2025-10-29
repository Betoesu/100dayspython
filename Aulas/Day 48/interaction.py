from selenium import webdriver
from selenium.webdriver.common.by import By

#Mantem o chrome aberto dps do programa terminar
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

community_portal = driver.find_element(By.LINK_TEXT,value="Community portal")
# community_portal.click()

search = driver.find_element(By.ID, "searchInput")
search.send_keys("Jesus")