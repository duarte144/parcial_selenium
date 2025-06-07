
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/broken")
time.sleep(2)  

print("Verificando imagenes...\n")
images = driver.find_elements(By.TAG_NAME, "img")

for img in images:
    src = img.get_attribute("src")
    if src:
        try:
            response = requests.get(src)
            print(f"SRC image: {src}")
            print(f"Status code: {response.status_code}")
            if response.status_code == 200:
                print("Imagen valida.\n")
            else:
                print("Imagen rota.\n")
        except Exception as e:
            print(f"Error al verificar imagen: {e}\n")

print("Verificando enlaces...\n")
links = driver.find_elements(By.TAG_NAME, "a")

for link in links:
    href = link.get_attribute("href")
    if href:
        try:
            response = requests.get(href)
            print(f"HREF link: {href}")
            print(f"Status code: {response.status_code}")
            if response.status_code == 200:
                print("Enlace valido.\n")
            else:
                print("Enlace roto.\n")
        except Exception as e:
            print(f"Error al verificar enlace: {e}\n")

driver.quit()
