from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/dynamic-properties")

texto_id_random = driver.find_element(
    By.XPATH, "//p[text()='This text has random Id']"
)
print(texto_id_random.get_attribute("id"))

btn_cambio_color = driver.find_element(By.ID, "colorChange")
classes_antes = btn_cambio_color.get_attribute("class")
time.sleep(6)
classes_despues = btn_cambio_color.get_attribute("class")

if "text-danger" not in classes_antes and "text-danger" in classes_despues:
    print("El botón cambió de color")
else:
    print("El botón no cambió de color")

try:
    boton_visible = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "visibleAfter"))
    )
    print("El botón 'Visible After 5 Seconds' está visible.")
except TimeoutException:
    print("El botón 'Visible After 5 Seconds' NO apareció.")

driver.quit()
