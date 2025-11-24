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

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")


booked_classes = 0
joined_waitlists = 0
already_booked_or_waitlisted = 0

processed_classes = []

for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    if "Tue" in day_title or "Thu" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

            class_info = f"{class_name} on {day_title}"

            # Check if already booked
            if button.text == "Booked":
                print(f"✓ Already booked: {class_info}")
                already_booked_or_waitlisted += 1
                processed_classes.append(f"[Booked] {class_info}")

            elif button.text == "Waitlisted":
                print(f"✓ Already on waitlist: {class_info}")
                already_booked_or_waitlisted += 1
                processed_classes.append(f"[Already on Waitlist] {class_info}")

            elif button.text == "Book Class":
                # Book the class
                button.click()
                print(f"✓ Successfully booked: {class_info}")
                booked_classes += 1
                processed_classes.append(f"[New Booking] {class_info}")

            elif button.text == "Join Waitlist":
                # Join waitlist if class is full
                button.click()
                print(f"✓ Joined waitlist for: {class_info}")
                joined_waitlists += 1
                processed_classes.append(f"[New Waitlist] {class_info}")
                
my_bookings_nav = driver.find_element(By.XPATH, "//*[@id='my-bookings-link']")
my_bookings_nav.click()
            
            

    




# print("\n--- BOOKING SUMMARY ---")
# print(f"Classes booked: {booked_classes}")
# print(f"WaitLists Joined: {joined_waitlists}")
# print(f"Already booked/waitlisted: {already_booked_or_waitlisted}")
# print(f"Total Tuesday and Thursday 6pm classes processed: {booked_classes + joined_waitlists + already_booked_or_waitlisted}")

# print("\n--- DETAILED CLASS LIST ---")
# for class_detail in processed_classes:
#     print(f"  • {class_detail}")


