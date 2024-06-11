from dependencies import driver, pyautogui, time, By, pyperclip
import login


def links():

    login.main()

    post_links = []

    #dots_buttons = driver.find_elements(By.CSS_SELECTOR, ".feed-shared-control-menu__trigger.artdeco-button.artdeco-button--tertiary.artdeco-button--muted.artdeco-button--1.artdeco-button--circle.artdeco-dropdown__trigger.artdeco-dropdown__trigger--placement-bottom.ember-view")

    for i in range(1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(3)

    dots_buttons = driver.find_elements(By.CSS_SELECTOR,
                                        ".feed-shared-control-menu__trigger.artdeco-button.artdeco-button--tertiary.artdeco-button--muted.artdeco-button--1.artdeco-button--circle.artdeco-dropdown__trigger.artdeco-dropdown__trigger--placement-bottom.ember-view")

    pyautogui.press('home')
    time.sleep(2)

    for button in dots_buttons:
        try:
            button.click()
            time.sleep(2)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('enter')
            time.sleep(1)
            link = pyperclip.paste()
            post_links.append(link)
            time.sleep(2)
        except:
            pass


    return post_links
    #for link in links:
        #print(link)