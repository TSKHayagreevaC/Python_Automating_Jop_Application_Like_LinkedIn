from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os

LOGIN_EMAIL = os.My_EMAIL
LOGIN_PASSWORD = os.My_PASSWORD
MOBILE_NUMBER = os.MY_MOBILE_NUMBER

chrome_driver_path = "/Users/SRIKANTHHAYAGREEVA/pycharm/projects"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords="
           "python%20developer&location=Hyderabad%2C%20India%2C%20United%20Kingdom&redirect="
           "false&position=1&pageNum=0")

time.sleep(2)
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

# loading the page
time.sleep(5)
email_field = driver.find_element_by_id("username")
email_field.send_keys(LOGIN_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(LOGIN_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)

all_listings = driver.find_elements_by_css_selector(".job-card-contianer--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # locating apply button
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # filling the mobile number
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(MOBILE_NUMBER)

        # Submit the application
        submit_button = driver.find_element_by_css_selector("footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()


