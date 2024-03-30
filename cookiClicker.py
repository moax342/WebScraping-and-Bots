from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie=driver.find_element(By.ID,'cookie')


clicker_money=int(driver.find_element(By.XPATH, '/html/body/div[3]/div[5]/div/div[1]/b').text.split(" -")[1])
while True:
    money = int(driver.find_element(By.ID, "money").text)
    cookie.click()
    if money >= clicker_money:
        driver.find_element(By.ID, 'buyCursor').click()
