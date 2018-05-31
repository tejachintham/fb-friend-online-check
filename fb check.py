import getpass
import os
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from tkinter import *
from  tkinter import ttk
from  tkinter import messagebox
print('\nFacebook Online Friends')

while(1):
    location = "D:\chromedriver_win32\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = location
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(location, chrome_options=chrome_options)
    driver.set_window_size(1920, 1080)
    print('Logging into Facebook...')
    driver.get('https://www.facebook.com/')
    emailBox = driver.find_element_by_id('email')
    emailBox.send_keys("tejachintham@gmail.com")
    passwordBox = driver.find_element_by_id('pass')
    passwordBox.send_keys("password")
    driver.find_element_by_id('loginbutton').click()
    time.sleep(35)
    aa = []
    aa = driver.find_elements_by_class_name("_55lp")
    on = []
    for a in aa:    
        p = a.get_attribute('innerHTML')
        z = []
        z = p.split("div")
        #print(z)
        pd = z[11].split(">")
        dt = pd[1].split("<")
        sd = z[7]
        if (sd == """ class="_568-"></"""):
            on.append(dt[0])
    driver.quit()        
    print(on)
    for oss in on:
         if (oss == "SH Reddy"):
             messagebox.showinfo(title="online", message="SH is online")
    time.sleep(120)

    
