from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# chrome_driver_path = "C:/Development/chromedriver"

driver = webdriver.Firefox()
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Challenge fill a newsletter form
fname_input=driver.find_element(By.NAME,"fName")
fname_input.send_keys("Mohammed")
fname_input.send_keys(Keys.ENTER)
lname_input=driver.find_element(By.NAME,"lName")
lname_input.send_keys("Abdallah")
lname_input.send_keys(Keys.ENTER)
email=driver.find_element(By.NAME, "email")
email.send_keys("max@outlook.com")
email.send_keys(Keys.ENTER)
submet = driver.find_element(By.PARTIAL_LINK_TEXT,"Sign Up")
submet.click()

# Challenge finding the events in the python.org
date = driver.find_elements(By.CSS_SELECTOR,'.event-widget time')
event = driver.find_elements(By.CSS_SELECTOR,'.event-widget ul a')

dates=[e.text for e in date]
events=[e.text for e in event]

dict_events={}
for _ in range(0,5):
    dict_events[_]={
        "time":dates[_],
        "Event":events[_]
    }
print(dict_events)