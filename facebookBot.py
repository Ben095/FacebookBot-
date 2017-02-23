from selenium import webdriver 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import json
from bs4 import BeautifulSoup
usr = "username"
pwd = "password"

chromeDriver = '/usr/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get("http://www.facebook.org")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(usr)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
sleep(10)
driver.get("https://www.facebook.com/search/latest/?q=%23blacklivesmatter")
sleep(4)
wait = WebDriverWait(driver, 10)

find_elem = None
scroll_from = 0
scroll_limit = 3000
while not find_elem:
    sleep(2)
    driver.execute_script("window.scrollTo(%d, %d);" %(scroll_from, scroll_from+scroll_limit))
    scroll_from += scroll_limit
    try:
        find_elem = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '7 mins')]")))
    except TimeoutException:
        pass
driver.close()

oct_5_elem = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '50 mins')]")))


html = driver.page_source
soup = BeautifulSoup(httpstml)
html = driver.page_source
text = driver.find_element(By.XPATH('//*[contains(text(), "11 mins")]'))
driver.execute_script("arguments[0].scrollIntoView(true);",text);
soup = BeautifulSoup(html)
getUserPosts = soup.findAll('div',attrs={'class':"userContentWrapper _5pcr"})
arr = []
for timeDate in getUserPosts:
	sess.exec_script("scroll(0, 250);")
	dictionary = {}
	try:
		dictionary['post'] = timeDate.find('div',attrs={'class':'_5pbx userContent'}).text
	except AttributeError:
		dictionary['post'] = "None"
	try:
		dictionary['time'] = timeDate.find('span',attrs={'class':'timestampContent'}).text
	except AttributeError:
		dictionary['time'] = "None"
	try:
		dictionary['share'] = timeDate.find('div',attrs={'class':'_36_q'}).text
	except AttributeError:
		dictionary['share'] = "None"
	try:
		dictionary['likes'] = timeDate.find('span',attrs={'class':'_4arz'}).text
	except AttributeError:
		dictionary['likes'] = "None"
	try:
		dictionary['userURL'] = timeDate.find('span',attrs={'class':'fwb'}).find('a')['href']
	except AttributeError:
		dictionary['userURL'] = "None"
	try:
		dictionary['imgURL'] = timeDate.find('div',attrs={'class':'_3-_h'}).find('img')['style'].replace('background-image: url(','').replace(');','')
	except AttributeError:
		dictionary['imgURL'] = "None"
	arr.append(dictionary)

with open('data.json','wb') as outfile:
	json.dump(arr,outfile,indent=4)
driver.close()