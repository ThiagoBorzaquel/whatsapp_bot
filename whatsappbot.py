from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)
contatos = ['Dev teste', 'Cris Bro']
