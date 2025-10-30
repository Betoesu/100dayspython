from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(chrome_options,)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name_input = driver.find_element(By.NAME,value="fName")
first_name_input.send_keys("Pedro")

last_name_input = driver.find_element(By.NAME,value="lName")
last_name_input.send_keys("Sarmento")

email_input = driver.find_element(By.NAME,value="email")
email_input.send_keys("p@gmail.com")

sing_up_button = driver.find_element(By.CLASS_NAME, value="btn")
sing_up_button.click()