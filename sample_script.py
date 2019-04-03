from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lettuce import *
from time import sleep

driver = webdriver.Chrome("/Users/andersontaylor/PythonPractice/Sample Test/chromedriver")

class sample_script(object):

    @after.all
    def tearDownClass(total):
        driver.quit()

    @step(u'Given I am on the login page')
    def given_i_am_on_the_login_page(step):
        driver.get("file:///Users/andersontaylor/PythonPractice/Sample Test/login.html")

    @step(u'And I enter valid credentials')
    def and_i_enter_valid_credentials(step):
        email = driver.find_element_by_id("email")
        password = driver.find_element_by_id("password")
        email.send_keys("coding@project.com")
        password.send_keys("Coding@123")
        submit = driver.find_element_by_id("submit")
        submit.click()

    @step(u'Then I should see a login successful alert')
    def then_I_should_see_a_login_successful_alert(step):
        alert = driver.switch_to_alert()
        alert_text = alert.text
        login_success = str("Login Successful")
        if (login_success in alert_text):
            print("Test Passed")
            alert.accept()
            return True
        else:
            print("Test Failed")
            alert.accept()
            return False

    @step(u'And I enter an invalid email')
    def and_i_enter_an_invalid_email(step):
        email = driver.find_element_by_id("email")
        password = driver.find_element_by_id("password")
        email.send_keys("fake@email.com")
        password.send_keys("Coding@123")
        submit = driver.find_element_by_id("submit")
        submit.click()

    @step(u'Then I should see an invalid email message')
    def then_i_should_see_an_invalid_email_message(step):
        alert = driver.switch_to_alert()
        alert_text = alert.text
        email_invalid = str("Wrong email address")
        if(email_invalid in alert_text):
            print("Test Passed")
            alert.accept()
            return True
        else:
            print("Test Failed")
            alert.accept()
            return False

    @step(u'And I enter a valid email')
    def and_i_enter_a_valid_email(step):
            email = driver.find_element_by_id("email")
            email.send_keys("coding@project.com")

    @step(u'And I enter an invalid password')
    def and_i_enter_an_invalid_password(step):
        login_attempts = int(0)
        password = driver.find_element_by_id("password")
        password.send_keys("password")
        submit = driver.find_element_by_id("submit")
        while(login_attempts < 2):
            submit.click()
            alert = driver.switch_to_alert()
            alert_text = alert.text
            invalid_pass = str("Email address and password do not match.")
            if(invalid_pass in alert_text):
                alert.accept()
                login_attempts+=1
                continue
            else:
                print("Test Failed")
                alert.accept()
                return False

        if(login_attempts == 2):
            submit.click()
            alert = driver.switch_to_alert()
            alert_text = alert.text
            invalid_pass_attempt_3 = str("You only have one more chance.")
            if(invalid_pass_attempt_3 in alert_text):
                alert.accept()
                login_attempts+=1
            else:
                print("Test Failed")
                alert.accept()
                return False

        if(login_attempts == 3):
            submit.click()
            alert = driver.switch_to_alert()
            alert_text = alert.text
            invalid_pass_attempt_4 = str("Your email address is locked and invalid.")
            if(invalid_pass_attempt_3 in alert_text):
                print("Test Passed")
                alert.accept()
                return True
            else:
                print("Test Failed")
                alert.accept()
                return False

    @step(u'And I click on the Need Help link')
    def and_i_click_on_the_need_help_link(step):
        need_help = driver.find_element_by_partial_link_text("Need Help?")
        need_help.click()

    @step(u'Then I should be taken to the FAQ page')
    def then_i_should_be_taken_to_the_faq_page(step):
        url = str(driver.current_url)
        if("faq.html" in url):
            print("Test Passed")
            return True
        else:
            print("Test Failed")
            return False
