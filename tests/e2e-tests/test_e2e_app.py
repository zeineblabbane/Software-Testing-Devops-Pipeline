from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import sqlite3
import time
from app import main
import multiprocessing
import os

#to run the test:
#coverage run -m unittest "e2e Test\test_e2e_app.py"

def deleteUser():
    database_filename = 'db_web.db'
    connection = sqlite3.connect(database_filename)
    connection.execute(
        "DELETE FROM USER WHERE USERNAME LIKE ?;", ("test",))
    connection.commit()
    connection.close()

class TestApp(TestCase):

    @classmethod
    def setUpClass(inst):
        inst.app_process=multiprocessing.Process(target=main,name="App",args=('test_database.db',True,))
        inst.app_process.start()
        time.sleep(1)
        inst.start = time.time()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--disable-gpu')
        inst.driver = webdriver.Chrome(r"C:\Users\DELL\Downloads\webdrivers\chromedriver.exe")

        print("Visiting index page")
        inst.driver.get('http://localhost:5000/')

    def test_01_add_user(self):
        print("Visiting add user page")
        adduser_button = self.driver.find_element(by=By.ID, value='Add')
        adduser_button.click()

        print("Filling user info")
        username_field = self.driver.find_element(by=By.ID, value='uname')
        username_field.send_keys('test')
        time.sleep(1)
        contact_field = self.driver.find_element(by=By.ID, value='contact')
        contact_field.send_keys('12345678')
        time.sleep(1)

        print("Submitting add user form")
        adduser_button = self.driver.find_element(by=By.ID, value='Submit')
        adduser_button.click()

        print("Redirecting to index page")
        message = self.driver.find_element(by=By.ID, value='message0').text
        expected_message = "User Added"

        self.assertIn(expected_message, message)

    def test_02_users_list(self):
        print("Checking user list page elements")
        table_id = self.driver.find_element(by=By.ID, value='test')
        rows = table_id.find_elements(By.TAG_NAME, "tr")
        col = rows[1].find_elements(By.TAG_NAME, "td")
        cd_data={
            "id":col[0].text,
            "uname": col[1].text,
            "contact": col[2].text
        }
        expected_cd_data = {
            "id": "1",
            "uname": "test",
            "contact": "12345678"
        }

        self.assertEqual(expected_cd_data,cd_data)

    def test_03_edit_username(self):
        edituser_button = self.driver.find_element(by=By.ID, value='Edit')
        edituser_button.click()

        print("Filling edit user form")
        uname_field = self.driver.find_element(by=By.ID, value='uname')
        uname_field.clear()
        uname_field.send_keys('test')

        print("Submitting add user form")
        edituser_button = self.driver.find_element(by=By.ID, value='Submit')
        edituser_button.click()

        print("Redirecting to index page")
        message = self.driver.find_element(by=By.ID, value='message0').text
        expected_message = "User Updated"
        table_id = self.driver.find_element(by=By.ID, value='test')
        rows = table_id.find_elements(By.TAG_NAME, "tr")
        col = rows[4].find_elements(By.TAG_NAME, "td")
        user_name = col[2].text
        expected_user_name = "Foulen"

        self.assertIn(expected_message, message)
        self.assertEqual(expected_user_name, user_name)

    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()
        deleteUser()
        inst.app_process.terminate()
        os.remove('test_database.db')



