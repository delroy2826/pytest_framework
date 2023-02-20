# Open Browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Go to web page
time.sleep(5)
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.fullscreen_window()
time.sleep(5)

# Type username student into Username field
driver.find_element(By.XPATH,'//input[@id="username"]').send_keys('student')
time.sleep(5)
# Type password Password123 into Password field
driver.find_element(By.XPATH,'//input[@id="password"]').send_keys('Password123')
time.sleep(2)
# Push Submit button
driver.find_element(By.XPATH,"//button[text()='Submit']").click()
time.sleep(2)
# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
actual_url = driver.current_url
expected_url = "https://practicetestautomation.com/logged-in-successfully/"
assert actual_url == expected_url
if actual_url == expected_url:
    print("Pass")
else:
    print("Fail")

#Verify new page contains expected text ('Congratulations' or 'successfully logged in')
actualText = driver.find_element(By.XPATH,"//h1[text()='Logged In Successfully']").text
expectedText = 'Logged In Successfully'
assert actualText == expectedText
if driver.find_element(By.XPATH, "//h1[text()='Logged In Successfully']").is_displayed():
    print("Logged In Successfully is Displayed")
else:
    print("Logged In Successfully is not Displayed")

#Verify button Log out is displayed on the new page
logoutbtn = driver.find_element(By.XPATH,"//a[text()='Log out']")
if logoutbtn.is_displayed():
    logoutbtn.click()
    print("Logout Button is displayed")
else:
    print("Logout Button is not displayed")

if driver.find_element(By.XPATH,'//section[@id="login"]//h2[text()="Test login"]').is_displayed():
    print("Login page is Displayed")
else:
    print("Login page is not displayed")


