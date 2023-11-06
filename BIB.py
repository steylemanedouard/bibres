
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver_service = Service(executable_path="C:\\Users\\steyl\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
from datetime import datetime, timedelta
current_datetime = datetime.now()
future= current_datetime + timedelta(days=7)
begin=  future.strftime(f'{future.year}-{future.month}-{future.day}T10:00:00')
eind=  future.strftime(f'{future.year}-{future.month}-{future.day}T17:00:00')
site= "https://www-sso.groupware.kuleuven.be/sites/KURT/Pages/NEW-Reservation.aspx?StartDateTime="+begin+"&EndDateTime="+eind+"&ID=303889&type=b&sessionId=aca52710-a05e-4b65-a92e-6e28cbbdde1e"
driver.get(site)
username = "r0886838"
password = "Edourd2521"
driver.implicitly_wait(200)


driver.find_element("id","username").send_keys(username)
driver.find_element("id","password").send_keys(password)
driver.find_element("id","pwdLoginBtn").click()
try:
    checkbox = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "complyConditionsCheckbox"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", checkbox)
    checkbox.click()

except TimeoutException:
    print("Timed out waiting for the checkbox to appear")
driver.find_element("id","submitReservationButton").click()
sleep(5)
driver.quit()

