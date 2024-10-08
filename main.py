from selenium import webdriver
from selenium.webdriver.common.by import By
# Below code is used to run scripts on brave browser-----------------------------------------

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

# brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
# chromedriver_path = "C:/Python/chromedriver.exe"
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = brave_path
# chrome_options.add_experimental_option("detach",True)
#
# service = Service(chromedriver_path)
# driver = webdriver.Chrome(options=chrome_options,service=service)

#----------------------------------------------------------------------------------

# URL = "https://www.amazon.in/dp/B0CGCZTYH2/ref=twister_B0CVQ9K5ZL?_encoding=UTF8&th=1"
#
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get(URL)
# price = driver.find_element(By.CLASS_NAME,value="a-price-whole").text
# print(price)
# # To get xpath, right clicking the piece of code we want to scrap and copying its xpath.
# emi_link = driver.find_element(By.XPATH,value='//*[@id="trigger_emioptions"]')
# print(emi_link.get_attribute(name="href"))
# driver.quit()



URl = "https://www.python.org/"
driver.get(URl)
menu = driver.find_element(By.CSS_SELECTOR,value=".medium-widget.event-widget.last ul")
raw_dates = menu.find_elements(By.TAG_NAME,value="time")
raw_text = menu.find_elements(By.TAG_NAME,value="a")
# dates = []
# events = []
events = {}
# for date in raw_dates:
#     date_text= date.text
#     dates.append(date_text)
#
# for text in raw_text:
#     event_text = text.text
#     events.append(event_text)

for i in range(len(raw_text)):
    events[i] = {
        "time": raw_dates[i].text,
        "name": raw_text[i].text
    }
print(events)
driver.quit()