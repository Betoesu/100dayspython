from selenium.webdriver.common.by import By
from constantes import USERNAME, PASSWORD, SIMILAR_ACCOUNT
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Importando erros para usar try e except
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException,
    ElementClickInterceptedException
)


class InstaFollower:
    def __init__(self):
        # Optional - Keep browser open (helps diagnose issues during a crash)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
    





    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        
        self.wait = WebDriverWait(self.driver, 20)

        try:
        #Espera o elemento estar na página para executar
            username = self.wait.until(EC.element_to_be_clickable((By.NAME,"username")))
            username.send_keys(USERNAME)

            password = self.driver.find_element(By.NAME, value="password")
            password.send_keys(PASSWORD)

            submit_button = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[3]/button')
            submit_button.click()

            #Espera aparecer om pop up de salvar informação
            salvar_info_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(text(), 'Agora não')]")))
            salvar_info_button.click()

            

        except (TimeoutException,NoSuchElementException):
            username = self.wait.until(EC.element_to_be_clickable((By.NAME,"email")))
            username.send_keys(USERNAME)

            password = self.driver.find_element(By.NAME, value="pass")
            password.send_keys(PASSWORD)

            submit_button = self.driver.find_element(By.XPATH, value='//*[@id="login_form"]/div/div[1]/div/div[3]/div/div/div/div[1]/div/span/span')
            submit_button.click()

            time.sleep(2)

            continuar_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,f"//span[contains(text(), {USERNAME})]")))
            continuar_button.click()

            #Espera aparecer om pop up de salvar informação
            salvar_info_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(text(), 'Agora não')]")))
            salvar_info_button.click()





        #Tempo para carregar sem erro
        time.sleep(3)








    def find_followers(self):

        #Clica em pesquisar
        pesquisa_button = self.driver.find_element(By.XPATH,'//*[@aria-label="Pesquisa"]')

        pesquisa_button.click()

        time.sleep(2)

        #Digita o nome da conta que se deseja ver os seguidore
        pesquisa_input = self.driver.find_element(By.XPATH, '//*[@aria-label="Entrada da pesquisa"]')

        pesquisa_input.send_keys(SIMILAR_ACCOUNT)

        
        
        #Clica no perfil escolhido
        conta_escolhida = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@href="/vinlandsaga_official/"]')))
        conta_escolhida.click()

        time.sleep(2)

        #Clica na aba de seguidores
        seguidores = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/vinlandsaga_official/followers/"]')))
        seguidores.click()

       

        time.sleep(5)
        modal_xpath = "/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
        modal = self.wait.until(EC.presence_of_element_located((By.XPATH, modal_xpath)))
        for n_account in range(2,10):
                xpath = f'//div[@role="dialog"]/div/div[2]/div/div/div[3]/div[1]/div/div[{n_account}]/div/div/div/div[3]/div/button'
                follow_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
                follow_button.click()
                time.sleep(2)

                botão_seguido_ou_solicitado = self.driver.find_element(By.XPATH,f'//div[@role="dialog"]/div/div[2]/div/div/div[3]/div[1]/div/div[{n_account}]/div/div/div/div[3]/div/button/div/div')
                seguido_ou_solicitado = botão_seguido_ou_solicitado.text


                if seguido_ou_solicitado == "Seguindo" or seguido_ou_solicitado == "Solicitado":
                    #Maneira com JavaScript de scrollar a tela
                    self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)






    def follow(self):
        pass
