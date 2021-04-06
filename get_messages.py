import requests
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
print("""
This tool can download all messages in social network vk.com.
For downloading messages we use selenium and python requests.
Enter login,password and count of messages for downloading(we don't save this data).\n
For using you should save cookie for login(If not choose time for solve captcha).
""")
TELEPHONE = str(input("Enter login or telephone number for vk:"))
PASSWORD = str(input("Enter password for vk:"))
COUNT_OF_MESSAGES = str(input("How many messages do you need to download:"))
TIME_FOR_CAPTCHA = str(input("Enter time for solving captcha(in seconds):"))

telephone= f"{TELEPHONE}"
password = f"{PASSWORD}"
count_of_messages = int(COUNT_OF_MESSAGES)

browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://vk.com")
browser.maximize_window()
cookies = browser.get_cookies()
session = requests.Session()
for cookie in cookies:
    session.cookies.set(cookie['name'],cookie['value'])
telephone_element = browser.find_element_by_id('index_email')
password_element = browser.find_element_by_id('index_pass')
btn_element = browser.find_element_by_id('index_login_button')
telephone_element.send_keys(telephone)
password_element.send_keys(password)
time.sleep(1)
btn_element.click()
time.sleep(int(TIME_FOR_CAPTCHA)+1)
browser.get("https://vk.com/im")
for i in range(1,count_of_messages):
    el = browser.find_element_by_xpath(f"//*[@id='im_dialogs']/li[{i}]")
    time.sleep(1)
    el.click()
    time.sleep(0.5)
    while True:
        pageHeight = browser.execute_script("return window.pageYOffset+window.innerHeight")
        if pageHeight<=710 and pageHeight>=654:
            print("break")
            break
        else:
            browser.execute_script("window.scrollBy(0,-1000)")
            time.sleep(0.5)
            print("scrolled")
    time.sleep(1)
    pyautogui.hotkey('ctrl','s')
    time.sleep(1)
    pyautogui.typewrite(f"Messenger{i}.html")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(0.5)
    el_back = browser.find_element_by_xpath("//*[@id='content']/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[1]/a")
    time.sleep(0.5)
    el_back.click()
    time.sleep(0.5)
    browser.execute_script("window.scrollBy(0,70)")
    time.sleep(0.5)
print("The script was ended")
