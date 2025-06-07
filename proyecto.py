from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 3)  

try:
    driver.get("http://127.0.0.1:8000/propietarios/")
    
    crear_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Crear Propietario")))
    crear_btn.click()
    time.sleep(3)

    nombre_input = wait.until(EC.presence_of_element_located((By.NAME, "nombre")))
    nombre_input.clear()
    nombre_input.send_keys("José Luis Duarte")
    time.sleep(3)

    direccion_input = wait.until(EC.presence_of_element_located((By.NAME, "direccion")))
    direccion_input.clear()
    direccion_input.send_keys("Calle Principal 456")
    time.sleep(3)

    telefono_input = wait.until(EC.presence_of_element_located((By.NAME, "telefono")))
    telefono_input.clear()
    telefono_input.send_keys("3126300")
    time.sleep(3)
    
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    email_input.clear()
    email_input.send_keys("josepachon@gmail.com")
    time.sleep(3)
    
    form = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "form")))
    form.submit()
    
    wait.until(
        EC.any_of(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Propietario registrado"),
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Éxito")
        )
    )
    
    print("Registro exitoso")

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
