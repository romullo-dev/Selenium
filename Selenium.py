from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time

# Abrir o navegador
navegador = webdriver.Firefox()

# Acessar um site
navegador.get("https://romullo-dev.github.io/Sistema-de-Logistica/")

# Colocar em tela cheia
navegador.maximize_window()

# Escrever em um formulário
navegador.find_element("id", "login").send_keys("ROMULO.DNA")
navegador.find_element("id", "senha").send_keys("123456")

# Selecionar o botão e clicar
botao = navegador.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary.w-100.mt-3')
botao.click()

# Agora você pode pressionar ENTER em algum campo de texto ou em um elemento após o clique.
campo = navegador.find_element(By.ID, "campo_ou_elemento_que_aceita_entrada")
campo.send_keys(Keys.ENTER)


time.sleep(20)

