import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

headless = webdriver.ChromeOptions()
headless.add_argument("--headless")

driver = webdriver.Chrome(options=headless)

driver.get("https://www.saucedemo.com/v1/index.html")

standard_user = driver.find_element(By.XPATH, "//div[@id='login_credentials']")

#User Set up
List_of_Users = str(standard_user.text).split(":")
List_of_Users_Name = List_of_Users[1]
individual_users = str(List_of_Users_Name).split("\n")

user_one = individual_users[1]

#Password Set up
User_Password = driver.find_element(By.CLASS_NAME, "login_password")
Split_user_passwd = str(User_Password.text).split(":")

current_user_passwd = Split_user_passwd[1]

driver.find_element(By.ID, "user-name").send_keys(user_one.strip())
driver.find_element(By.ID, "password").send_keys(current_user_passwd.strip())

driver.find_element(By.XPATH, "//input[@id='login-button']").click()

locator_id = (By.XPATH, "//div[@id='shopping_cart_container']")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located(locator_id))

driver.get_screenshot_as_file("homepage.png")

time.sleep(2)
driver.close()
