import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

i = 1
pocitadlo = 0
while True:
    i=1
    pocitadlo += 1
    driver = webdriver.Chrome()

    driver.get(
        "https://docs.google.com/forms/d/e/1FAIpQLScvBclavzzhzQPKhq-2fg3EWiabPdrGyDsFOSn0JaJ0SzaM-A/viewform?vc=0&c=0"
        "&w=1&flr=0")

    wait = WebDriverWait(driver, 10)
    questions_container = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='listitem']")))

    # Find all the question containers on the page
    questions = driver.find_elements(By.XPATH, "//div[@role='listitem']")

    # Loop through each question and randomly select an answer
    for question in questions:

        # Find all the radio buttons for this question
        radio_buttons = question.find_elements(By.XPATH, "//div[@role='radio']")
        print(f"Question {question.text} has {len(radio_buttons)} radio buttons.")
        if len(radio_buttons) == 0:
            print(f"Error: no radio buttons found for question {question.text}")
            continue
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='radio']")))
        # Randomly select one radio button to click
        random_radio_button = random.choice(radio_buttons[i:i + 3])
        random_radio_button.click()
        i = i + 4

    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Odoslať']")))

    # click on the button
    button.click()

    # Close the webdriver
    time.sleep(2)
    driver.quit()

    # check if the condition is met and break out of the loop if it is
    if pocitadlo == 5:
        break
