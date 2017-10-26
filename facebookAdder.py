#! /usr/bin/env python3
# facebookadder.py - Automated Facebook Friend Adding in a browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from threading import Thread

#TODO make it run with arguments from terminal
email = ""
password = ""
seed = "westedcrean"
#STEP 1: SETUP
driver = webdriver.Chrome()                                 #instance of Chrome WebDriver is created
driver.get("http://www.facebook.org")
#STEP 2: LOGIN or REGISTER
assert "Facebook" in driver.title
assert "zaloguj" in driver.title
elem = driver.find_element_by_id("email")
elem.clear()
elem.send_keys(email)
elem = driver.find_element_by_id("pass")
elem.clear()
elem.send_keys(password)
elem.send_keys(Keys.RETURN)

#STEP 2: GET TO A SEED PROFILE -> FRIENDLIST
driver.get("http://www.facebook.org/"+ seed + "/friends")
currentbutton = driver.find_element_by_class("FriendButton")

def generateFriendList(friend_amount):
    
    
    
