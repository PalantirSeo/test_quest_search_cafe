import json
import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def load_expected_result():
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filename = os.path.join(fileDir, 'src/expected_results.json')
    with open(filename, 'r', encoding='utf8') as f:
        json_data = json.loads(f.read())
    return json_data


@pytest.fixture(scope="function")
def load_locators():
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filename = os.path.join(fileDir, 'src/locators.json')
    with open(filename, 'r') as f:
        json_data = json.loads(f.read())
    return json_data
