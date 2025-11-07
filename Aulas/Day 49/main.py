from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

ACCOUNT_EMAIL = "pedro@test.com"
ACCOUNT_PASSWORD = "teste123teste"
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)

# Navigate to site
driver.get(GYM_URL)


wait = WebDriverWait(driver,2)

login_botton =  wait.until(ec.element_to_be_clickable((By.ID,"login-button")))
login_botton.click()


email_input = wait.until(ec.presence_of_element_located((By.ID,"email-input")))
email_input.send_keys(ACCOUNT_EMAIL)


password_input = wait.until(ec.presence_of_element_located((By.ID,"password-input")))
password_input.send_keys(ACCOUNT_PASSWORD)


submit_button = driver.find_element(by=By.ID,value="submit-button")
submit_button.click()


schedule_page = wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))
tuesday_days = schedule_page.find_elements(By.CSS_SELECTOR,"[id^='day-group-tue']")

for group in tuesday_days:
    try:
        tuesday_six_pm = group.find_element(By.CSS_SELECTOR, "[id*='1800']")
        six_pm_button = tuesday_six_pm.find_element(By.CSS_SELECTOR, "button")
        task_name = tuesday_six_pm.find_element(By.CSS_SELECTOR, "div div h3").text

        six_pm_button.click()
        print(f"✅Booked {task_name} on {}")
        break  # se achou e clicou, sai do loop
    except:
        continue  # se não achou nesse grupo, tenta o próximo


