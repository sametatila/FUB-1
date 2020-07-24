from selenium import webdriver
import time
#Declare some variables for URLs.
urrr = "https://www.threadless.com/join/"
urrr2 = "https://www.threadless.com/profile/artist_dashboard/artist-shop/products/create/"
#Run the chromium
driver = webdriver.Chrome("C:\ytw\chromedriver.exe")
#Open the website
driver.get(urrr)
#Fill the username box
username1 = driver.find_element_by_xpath('//*[@id="id_username"]')
username1.send_keys("sametatila@gmail.com")
#Fil
pass1 = driver.find_element_by_xpath('//*[@id="id_password"]')
pass1.send_keys("Linkin.123!")
loginbutton = driver.find_element_by_xpath('//*[@id="login_form"]/fieldset/input[2]')
loginbutton.click()
time.sleep(5)
driver.get(urrr2)
time.sleep(5)
picture = "C:\ytw\Ay.png"
upload1 = driver.find_element_by_name("upload")
upload1.send_keys("C://ytw/Ay.png")


