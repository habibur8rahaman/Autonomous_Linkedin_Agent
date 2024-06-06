from dependencies import driver, Keys, By, time

def main():
    with open('credentials.txt', 'r') as credentials:
        username = credentials.readline()
        password = credentials.readline()


    driver.maximize_window()

    driver.get("https://www.linkedin.com/feed/")

    enter_username = driver.find_element(By.ID, "username")
    enter_username.send_keys(username)
    enter_password = driver.find_element(By.ID, "password")
    enter_password.send_keys(password)

    enter_password.send_keys(Keys.ENTER)

    time.sleep(15)

    #return driver