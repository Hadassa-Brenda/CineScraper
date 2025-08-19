from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BrowserManager:
    def __init__(self, wait_time=20):
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, wait_time)

    def open(self, url: str):
        self.driver.get(url)

    def wait_for(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def wait_for_all(self, by, value):
        return self.wait.until(EC.presence_of_all_elements_located((by, value)))

    def quit(self):
        self.driver.quit()