from selenium.webdriver.common.by import By
from constantes import USERNAME, PASSWORD, SIMILAR_ACCOUNT
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class InstaFollower:
    def __init__(self):
        # Optional - Keep browser open (helps diagnose issues during a crash)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
    

    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        
        wait = WebDriverWait(self.driver, 20)

        #Espera o elemento estar na página para executar
        username = wait.until(EC.element_to_be_clickable((By.NAME,"username")))
        username.send_keys(USERNAME)

        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(PASSWORD)

        submit_button = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[3]/button')
        submit_button.click()

        
        #Espera aparecer om pop up de salvar informação
        salvar_info_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(text(), 'Agora não')]")))
        salvar_info_button.click()

        #Tempo para carregar sem erro
        time.sleep(5)



    def find_followers(self):

        #Clica em pesquisar
        pesquisa_button = self.driver.find_element(By.XPATH,'//*[@aria-label="Pesquisa"]')

        pesquisa_button.click()

        time.sleep(2)

        #Digita o nome da conta que se deseja ver os seguidore
        pesquisa_input = self.driver.find_element(By.XPATH, '//*[@aria-label="Entrada da pesquisa"]')

        pesquisa_input.send_keys(SIMILAR_ACCOUNT)
        
        #Clica no perfil escolhido
        conta_escolhida = self.driver.find_element(By.XPATH,'//*[@href="/vinlandsaga_official/"]')
        conta_escolhida.click()

        time.sleep(2)

        #Clica na aba de seguidores
        seguidores = self.driver.find_element(By.XPATH, '//a[@href="/vinlandsaga_official/followers/"]')
        seguidores.click()

        #Falta clicar automaticamente para seguir e descobrir como scrollar para baixo
    def follow(self):
        pass
