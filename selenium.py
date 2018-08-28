from selenium import webdriver
from urllib import urllib
 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(chrome_options=options)
 
driver.get('http://imgur.com/')
 
images = driver.find_elements_by_tag_name('img')
for image in images:
    print(image.get_attribute('src'))
    urllib.urlretrieve(src, "filename.png")
driver.close()