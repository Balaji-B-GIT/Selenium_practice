from selenium import webdriver
from selenium.webdriver.common.by import By
# To press keyboard buttons like crtl,shift,enter etc we import.....
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
# URl = "https://en.wikipedia.org/wiki/Main_Page"
# driver.get(URl)
# count = driver.find_element(By.CSS_SELECTOR,value = "#articlecount a")
# print(count.text)
#
# # Select a link using link tag
# link = driver.find_element(By.LINK_TEXT,value = "Content portals")
#
# # clicking a link
# link.click()
#
# # Filling a text field and pressing enter
# search = driver.find_element(By.NAME,value = "search")
# search.send_keys("Python",Keys.ENTER)

URl = "https://secure-retreat-92358.herokuapp.com/"
driver.get(URl)

first = driver.find_element(By.NAME,value = "fName")
last = driver.find_element(By.NAME,value = "lName")
email = driver.find_element(By.NAME,value = "email")
button = driver.find_element(By.TAG_NAME,value="button")

first.send_keys("B")
last.send_keys("B")
email.send_keys("B@gmail.com")
button.click()