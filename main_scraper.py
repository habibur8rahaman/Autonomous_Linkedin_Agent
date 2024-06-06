from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui
import pyperclip
import requests



links = []

username = "your email"
password = "password"

driver = webdriver.Chrome()


def extracted_post(link):

    driver.get(link)
    time.sleep(10)

    text = driver.find_element(By.CLASS_NAME, "update-components-update-v2__commentary").text

    print(text)
    print('----------------------------------------')

    reacts = driver.find_element(By.CLASS_NAME, "social-detail-social-counts__count-icon--0").get_attribute('alt')

                                                #use "reactions-icon social-detail-social-counts__count-icon" for top 3 reactions


    print(reacts)
    print('========================================')

    if reacts == 'like':
        like = driver.find_element(By.CSS_SELECTOR, ".feed-shared-social-action-bar__action-button")
        like.click()

        time.sleep(3)

def scrap():


    driver.maximize_window()

    driver.get("https://www.linkedin.com/feed/")

    enter_username = driver.find_element(By.ID, "username")
    enter_username.send_keys(username)
    enter_password = driver.find_element(By.ID, "password")
    enter_password.send_keys(password)

    enter_password.send_keys(Keys.ENTER)

    time.sleep(15)


    #links = driver.find_elements(By.CLASS_NAME, "feed-shared-control-menu__trigger")

    #for i in range(2):

        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #time.sleep(2)

    dots_buttons = driver.find_elements(By.CSS_SELECTOR, ".feed-shared-control-menu__trigger.artdeco-button.artdeco-button--tertiary.artdeco-button--muted.artdeco-button--1.artdeco-button--circle.artdeco-dropdown__trigger.artdeco-dropdown__trigger--placement-bottom.ember-view")
    #post_section = driver.find_elements(By.CLASS_NAME, "feed-shared-update-v2__description")
    #react_section = driver.find_elements(By.CLASS_NAME, "update-v2-social-activity")

    #dots_buttons = [dots_buttons[0], dots_buttons[1], dots_buttons[2], dots_buttons[3], dots_buttons[4]]
    for button in dots_buttons:
        try:
            button.click()
            time.sleep(2)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('enter')
            time.sleep(1)
            link = pyperclip.paste()
            links.append(link)
            time.sleep(2)
        except:
            pass

    for link in links:
        extracted_post(link)




scrap()

