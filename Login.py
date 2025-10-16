from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5) 


try:
    # 1) Login
    driver.get('https://www.saucedemo.com')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

# 2) Validar que estamos en inventario
    assert '/inventory.html' in driver.current_url
 
 # 3) Verificar título de sección
    titulo = driver.find_element(By.CSS_SELECTOR,'div.header_secondary_container .title').text
    assert titulo == 'Products' 
    print('Título de sección OK →', titulo)
 
 # 4) Contar productos visibles
    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    print(f'Se encontraron {len(productos)} productos.')
 
finally:
    time.sleep(5)
    # driver.quit()