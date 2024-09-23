 #Source: https://www.youtube.com/watch?v=NB8OceGZGjA&list=WL&index=8&t=982s

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #allowing use of keys
from selenium.webdriver.support.ui import WebDriverWait #1 allow to wait for the presence of the element before going forward
from selenium.webdriver.support import expected_conditions as EC #2 allow to wait for the presence of the element before going forward
import time

service = Service(executable_path="C:\Program Files\chromedriver.exe")
driver = webdriver.Chrome(service=service)

webiste = "https://orteil.dashnet.org/cookieclicker/"
driver.get(webiste)


cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"


#Select Language
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
) #if after 5s the element doesn't exist, crash the program

language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()


#Click the cookie
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
) #if after 5s the element doesn't exist, crash the program

cookie = driver.find_element(By.ID, cookie_id)

while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))
    print(cookies_count)

    for i in range(4): #4 product
        #find the price
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")
        
        #make sure the product_price is string
        if not product_price.isdigit():
            continue
        
        product_price = int(product_price)

        #find the product, then click the button where the product is
        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break