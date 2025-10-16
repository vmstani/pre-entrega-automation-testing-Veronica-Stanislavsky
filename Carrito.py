from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuración del navegador
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Esperar página de inventario
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/inventory.html"))
    
    # 1️⃣ Agregar primer producto al carrito
    first_product_button = driver.find_element(By.CLASS_NAME, "btn_inventory")
    first_product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    first_product_button.click()
    
    # 2️⃣ Verificar contador del carrito
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_count == "1", f"Contador incorrecto: {cart_count}"
    print(f"Producto agregado al carrito. Contador: {cart_count} ✅")
    
    # 3️⃣ Navegar al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.url_contains("/cart.html"))
    
    # 4️⃣ Verificar que el producto esté en el carrito
    cart_product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert cart_product_name == first_product_name, "Producto en carrito incorrecto"
    print(f"Producto en carrito: {cart_product_name} ✅")

finally:
    time.sleep(5)
    #driver.quit()
