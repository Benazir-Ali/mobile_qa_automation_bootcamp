from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import logging
from driver import WebCommon

logging.basicConfig(filename="test_04.log")
log = logging.getLogger()


class Test04Android:
    driver = WebCommon("/Users/benazir/QTFProjects/theapp.apk")
    parent = WebElement
    child = []

    def test_04(self):
        self.app = self.driver.init_driver()

        self.parent = self.app.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup")
        self.child = self.parent.find_elements(By.XPATH, '//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView')

        self.driver.close_driver()

        log.info("List size: 7, expected: pass")
        assert len(self.child) == 7

