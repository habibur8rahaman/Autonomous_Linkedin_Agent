import pyautogui

from dependencies import driver, time, By
import sentiment_analysis
import sentiment_critic

import give_reaction



def extracted_post(link):

    driver.get(link)
    time.sleep(10)

    text = driver.find_element(By.CLASS_NAME, "update-components-update-v2__commentary").text

    #print(text)
    #print('----------------------------------------')

    sentiment = sentiment_analysis.main(text)

    print(sentiment)

    print('----------------------------------------')

    reacts = driver.find_elements(By.CLASS_NAME, "social-detail-social-counts__count-icon")
    #react2 = driver.find_element(By.CLASS_NAME, "social-detail-social-counts__count-icon--1").get_attribute('alt')
    #react3 = driver.find_element(By.CLASS_NAME, "social-detail-social-counts__count-icon--2").get_attribute('alt')

    #reacts = [react1, react2, react3]

                                                #use "reactions-icon social-detail-social-counts__count-icon" for top 3 reactions

    #print('========================================')

    #critic_sentiment = sentiment_critic.main(text, sentiment, reacts)
    #print(critic_sentiment)
    #print('========================================')

    #if react1 == 'like':
    give_reaction.main(sentiment)



    #elif sentiment == ''