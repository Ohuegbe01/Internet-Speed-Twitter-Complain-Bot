from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10

TWITTER_EMAIL = ''
TWITTER_PASSWORD = ''
TWITTER_USERNAME = ''
#


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")


        accept_button = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        accept_button.click()

        time.sleep(3)

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        time.sleep(40)
        self.up = float(self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.down = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        print(self.up, self.down)

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/login')
        time.sleep(5)

        email = self.driver.find_element(By.CSS_SELECTOR, '.css-175oi2r input')
        email.send_keys(TWITTER_EMAIL)

        time.sleep(3)
        Next = self.driver.find_element(By.XPATH,
                                   '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        print(Next)
        Next.click()
        input('d')
        # if it asks for email verification then..
        # username
        time.sleep(3)
        username = self.driver.find_element(By.XPATH,
                                       '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        print(username)
        username.send_keys(TWITTER_USERNAME)

        # next
        time.sleep(3)
        n = self.driver.find_element(By.XPATH,
                                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        print(n)
        n.click()

        # password
        time.sleep(3)
        password = self.driver.find_element(By.XPATH,
                                       '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)

        # login
        login = self.driver.find_element(By.XPATH,
                                    '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
        login.click()

        # accept cookies
        time.sleep(5)
        accept = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/button[1]')
        accept.click()


        if self.up<40 and self.down<40:
            time.sleep(3)
            something = self.driver.find_element(By.XPATH,
                                            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            # something.send_keys(f'Hey internet provider, why is my internet speed {self.up}up and {self.down}down?')
            something.send_keys('@Cypher.nuel hafa')
            # post
            post = self.driver.find_element(By.XPATH,
                                       '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
            post.click()
            time.sleep(60)
        else:
            self.driver.quit()


bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
bot.tweet_at_provider()