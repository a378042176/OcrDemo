#encoding:utf8
from selenium import webdriver

browser = webdriver.Firefox()
url = "http://tp.52hom.com/tp/adminryx/verifycode1.asp"
# browser.set_window_size(1200, 900)
browser.get(url)

browser.save_screenshot("codingpy.png")
browser.close()

