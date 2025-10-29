from selenium import webdriver
from selenium.webdriver.common.by import By

#Manter o Chrome aberto depois do programa acabar
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")
 
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)  
# documentation_link = driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a") 
# print(documentation_link)

# donate_link = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[4]/p[2]/a[2]')
# print(donate_link.text)



#DESAFIO DICIONARIO DE EVENTOS DO PYTHON ORG |
#                                            v

time_without_year = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
event_times = []
for event_time in time_without_year:                                                                #<-- Maneira de conseguir o ano, pois ao usar o mesmo método do event_names nao era retornado o ano
    time = event_time.get_attribute("datetime").replace("T00:00:00+00:00", "")
    event_times.append(time)

event_names = driver.find_elements(By.CSS_SELECTOR,value='.event-widget li a')
events = {}

for n in range(len(event_names)):
    events[n] = {
        "time": event_times[n],
        "name": event_names[n].text,
    }
print(events)
driver.quit()

#Fecha o Chrome
# driver.close() #Fecha a página atual