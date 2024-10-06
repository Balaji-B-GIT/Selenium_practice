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

URL = "https://www.amazon.in/dp/B0CGCZTYH2/ref=twister_B0CVQ9K5ZL?_encoding=UTF8&th=1"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
price = driver.find_element(By.CLASS_NAME,value="a-price-whole").text
print(price)
driver.quit()