
from selenium.webdriver.common.by import By
import unittest
from selenium import webdriver
from time import sleep
import warnings
message = input('Write the message you are going to send: ')
while True:
    try:
        count = int(input("Enter the number of messages: "))
        break
    except ValueError:
        print("That's not a number, try again")

class spam_whatsapp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '/Users/pinjup_/Documents/spam_whatsapp/chromedriver') # <----------- Configure executable path
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://web.whatsapp.com")
        

    def test_spam(self):
        driver = self.driver
        #p_ = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div/div[18]')
        #p_.click()
        p_ = driver.implicitly_wait(300)
        n = 0
        while n < count:
            n+=1
            print(f"Se han enviado {n} mensajes")
            p_ = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div').send_keys(message)
            sleep(0.2)
            p_ = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
            p_.click()
            warnings.simplefilter('ignore', ResourceWarning)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
