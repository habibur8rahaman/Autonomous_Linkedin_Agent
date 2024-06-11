from dependencies import driver, By, pyautogui, time


def main(sentiment):

    if sentiment == 'like':
        like = driver.find_element(By.CSS_SELECTOR, ".feed-shared-social-action-bar__action-button")
        like.click()
        time.sleep(3)

    else:
        while True:
            try:
                like_location = pyautogui.locateCenterOnScreen('imgs/like.png', confidence = 0.9)
                time.sleep(3)
                pyautogui.moveTo(like_location)
                time.sleep(3)

                #x, y = pyautogui.locateCenterOnScreen('reacts.png')

                if sentiment == 'celebrate':
                    celebrate = pyautogui.locateCenterOnScreen('imgs/celebrate.png')
                    pyautogui.moveTo(celebrate)
                    pyautogui.click()

                elif sentiment == 'support':
                    support = pyautogui.locateCenterOnScreen('imgs/support.png')
                    pyautogui.moveTo(support)
                    pyautogui.click()

                elif sentiment == 'love':
                    love = pyautogui.locateCenterOnScreen('imgs/love.png')
                    pyautogui.moveTo(love)
                    pyautogui.click()

                elif sentiment == 'insightful':
                    insightful = pyautogui.locateCenterOnScreen('imgs/insightful.png')
                    pyautogui.moveTo(insightful)
                    pyautogui.click()

                elif sentiment == 'funny':
                    funny = pyautogui.locateCenterOnScreen('imgs/funny.png')
                    pyautogui.moveTo(funny)
                    pyautogui.click()

                time.sleep(3)

                break

            except:
                pyautogui.scroll(-500)
                time.sleep(5)
                pass

    #except:
    #    while counter < 5:
    #        pyautogui.scroll(-720)
    #        counter += 1
    #        break
    #    if counter != 5:
    #        main(sentiment)

