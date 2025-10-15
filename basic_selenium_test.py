import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging
logging.basicConfig(filename='selenium_test.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s:%(message)s')

# Path to your local index.html (update as needed)
INDEX_HTML_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../index.html'))
FILE_URL = f'file://{INDEX_HTML_PATH}'

# Chrome options for headless mode (optional)
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

try:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(FILE_URL)
    logging.info('Opened Todo List App at %s', FILE_URL)

    # Test Case 1: Add a valid task
    task_input = driver.find_element(By.ID, 'taskInput')
    add_button = driver.find_element(By.XPATH, '//button[contains(text(), "Add Task")]')
    task_input.clear()
    task_input.send_keys('Buy groceries')
    add_button.click()
    logging.info('Added task: Buy groceries')

    # Wait for the new task to appear
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.ID, 'taskList'), 'Buy groceries')
    )
    tasks = driver.find_elements(By.XPATH, '//ul[@id="taskList"]/li')
    assert any('Buy groceries' in t.text for t in tasks), 'Task not found in list!'
    logging.info('Verified task appears in list.')

    # Test Case 2: Attempt to add an empty task
    task_input.clear()
    add_button.click()
    # Wait for alert
    WebDriverWait(driver, 2).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert 'Please enter a task' in alert.text
    alert.accept()
    logging.info('Verified alert for empty input.')

    print('All Selenium tests passed.')
except Exception as e:
    logging.error('Test failed: %s', e)
    driver.save_screenshot('selenium_error.png')
    print('Test failed. See selenium_error.png and selenium_test.log for details.')
finally:
    driver.quit()
