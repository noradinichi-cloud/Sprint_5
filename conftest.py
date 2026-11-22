import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    yield chrome
    chrome.quit()
