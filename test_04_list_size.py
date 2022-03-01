from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import logging

logging.basicConfig(filename="test_04.log", level=logging.DEBUG)
log = logging.getLogger()


class WebCommon:
    def __init__(self, apk_name):
        self.apk_name = apk_name
        self.driver = None

    def init_driver(self):
        self.driver = self.get_driver()

    def get_driver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Tester'
        desired_caps['app'] = self.apk_name

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        return self.driver

    def close_driver(self):
        self.driver.quit()


class Test04Android:
    driver = WebCommon("/Users/benazir/QTFProjects/theapp.apk")
    parent = WebElement
    child = []

    def test_04(self):
        self.app = self.driver.get_driver()

        self.parent = self.app.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup")
        self.child = self.parent.find_elements(By.XPATH, '//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView')

        self.driver.close_driver()

        log.info("List size: 7, expected: pass")
        assert len(self.child) == 7

