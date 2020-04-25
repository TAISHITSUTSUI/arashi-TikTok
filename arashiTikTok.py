from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("https://www.tiktok.com/@arashi_5_official")


follow_number  = driver.find_element_by_xpath("//span[@class='number'][2]")

print('follower:'+(follower_number.text))
print ('follow: ' + (follow_number.text))
abs