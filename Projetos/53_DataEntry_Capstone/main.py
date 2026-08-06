from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from data_loader import load_soup
from data_identificador import extract_rent_listings
from data_entry import send_forms
from create_sheets import create_sheets


FORMS_LINK = "https://forms.gle/Se7zD7Uoh15MFZex8"
EDITOR_FORMS_LINK = 'https://docs.google.com/forms/d/1IS365Z7CDptFZPyYpNrrwYienpgjD-nFy8-voQrqpQs/edit'


def main():
    # Carrega dados
    soup = load_soup()
    rent_listings = extract_rent_listings(soup)

    # Configura Selenium
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(FORMS_LINK)

    wait = WebDriverWait(driver, 20)

    # Envia dados
    for address, price, link in rent_listings:  
        print(f"{address} | {price} | {link}")
        send_forms(driver, wait, address, price, link)

    create_sheets(EDITOR_FORMS_LINK)
    

    
        


if __name__ == "__main__":
    main()