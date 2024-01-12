from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3792366045&f_AL=true&origin=JOB_SEARCH_PAGE_JOB_FILTER")

sign_in = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()
time.sleep(3)

user_name = driver.find_element(By.NAME, value="session_key")
user_name.send_keys("hokmas745@gmail.com")
time.sleep(3)
password = driver.find_element(By.NAME, value="session_password")
password.send_keys("Mashok006@coc")
time.sleep(3)
login = driver.find_element(By.CSS_SELECTOR, value=".login__form_action_container button")
login.click()
time.sleep(7)
save = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button/span[1]')
save.click()



