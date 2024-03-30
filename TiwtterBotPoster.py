from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

EMAIL= "YOUR USER NAME"
PASSWORD= "YOUR PASSWORD"
driver = webdriver.Firefox()
driver.get("https://twitter.com/")

sleep(10)
sign_in = driver.find_element(By.PARTIAL_LINK_TEXT,"Sign in")
sign_in.click()
sleep(5)
email_input=driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]"
                                         "/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
email_input.send_keys(EMAIL)
next_button= driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]"
                                          "/div/div/div[2]/div[2]/div/div/div/div[6]")
next_button.click()
sleep(2)
pass_input=driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]"
                                        "/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]"
                                        "/div[1]/input")
pass_input.send_keys(PASSWORD)
log_in= driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]"
                                     "/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")
log_in.click()
sleep(3)
text_input=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div"
                                        "/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div"
                                        "/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]"
                                        "/div/div/div/div")
text_input.send_keys("new account ")