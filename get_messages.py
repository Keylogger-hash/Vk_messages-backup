import requests
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import sys
print("""
This tool can download all messages in social network vk.com.
For downloading messages we use selenium and python requests.
Enter login,password and count of messages for downloading(we don't save this data).\n
For using you should save cookie for login(If not choose time for solve captcha).
""")
# TELEPHONE = str(input("Enter login or telephone number for vk:"))
# PASSWORD = str(input("Enter password for vk:"))
# COUNT_OF_MESSAGES = str(input("How many messages do you need to download:"))
# TIME_FOR_CAPTCHA = str(input("Enter time for solving captcha(in seconds):"))
# PATH_TO_CHROMEDRIVER = str(input("Enter a path to chromedriver(%PATH%/chromedriver.exe):"))
#
# telephone= f"{TELEPHONE}"
# password = f"{PASSWORD}"
# count_of_messages = int(COUNT_OF_MESSAGES)
try:
    login=sys.argv[1]
    password=sys.argv[2]
    path_to_chromedriver=sys.argv[3]
    time_for_captcha=sys.argv[4]
    start_number_message=sys.argv[5]
    end_number_message=sys.argv[6]
except IndexError:
    print("Usage: python get_messages.py <login> <password> <path_to_chromedriver> <time_for_captcha> <start_number_message> <end_number_message")
print(path_to_chromedriver)
browser = webdriver.Chrome(path_to_chromedriver)
browser.get("https://vk.com")
browser.maximize_window()
cookies = browser.get_cookies()
session = requests.Session()
for cookie in cookies:
    session.cookies.set(cookie['name'],cookie['value'])
telephone_element = browser.find_element_by_id('index_email')
password_element = browser.find_element_by_id('index_pass')
btn_element = browser.find_element_by_id('index_login_button')
telephone_element.send_keys(login)
password_element.send_keys(password)
time.sleep(1)
btn_element.click()
time.sleep(int(time_for_captcha)+1)
browser.get("https://vk.com/im")
i=0
while i<10:
    browser.execute_script("window.scrollBy(0,10000)")
    time.sleep(0.5)
    i+=1

el = browser.find_element_by_xpath(f"//*[@id='im_dialogs']/li[{int(start_number_message)+2}]")
ActionChains(browser).move_to_element(el).perform()
time.sleep(0.5)
for i in range(int(start_number_message),int(end_number_message)):
    el = browser.find_element_by_xpath(f"//*[@id='im_dialogs']/li[{i}]")
    # ActionChains(browser).move_to_element(el).perform()
    time.sleep(1)
    el.click()
    time.sleep(0.5)
    endToScroll = browser.execute_script("return window.innerHeight")
    j = 0
    chat_name =  browser.find_element_by_xpath("//*[@id='content']/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[3]/div/span[1]/span/a").text
    print(f"{i} Chat:'{chat_name}'")
    while j<=5000:
        pageHeight = browser.execute_script("return window.pageYOffset+window.innerHeight")
        if pageHeight<=endToScroll:
            break
        else:
            j+=1
            browser.execute_script("window.scrollBy(0,-1000)")
            time.sleep(0.5)
    time.sleep(1)
    pyautogui.hotkey('ctrl','s')
    time.sleep(1)
    pyautogui.typewrite(f"Messenger{i}.html")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    el_back = browser.find_element_by_xpath("//*[@id='content']/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[1]/a")
    time.sleep(0.5)
    el_back.click()
    time.sleep(0.5)
    browser.execute_script("window.scrollBy(0,70)")
    time.sleep(0.5)
print("The script was ended")
