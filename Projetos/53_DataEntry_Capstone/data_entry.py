#Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



def send_forms(driver, wait, address, price, link) -> None:
    """
    Preenche o Google Forms com os dados do imóvel
    
    :param address: Endereco do Aluguel
    :param price: Preço do Aluguel
    :param link: Link do Aluguel

    Returns
        None
    """

    #Escrevendo o endereço
    address_input = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    address_input.send_keys(address)

    #Escrevendo o preço
    price_input = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    price_input.send_keys(price)

    #Escrevendo o link
    link_input = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    link_input.send_keys(link)

    #Botão Enviar
    submit_button = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_button.click()

    #Botão Enviar outra resposta
    submit_again_button = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
    submit_again_button.click()

 
