from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from driver import WebCommon
from datetime import datetime


class Test07Android:
    def setup_method(self):
        self.driver = WebCommon("/Users/benazir/QTFProjects/theapp.apk")
        self.app = self.driver.init_driver()

    def wait(self, timeout):
        self.start = datetime.now()
        while (datetime.now() - self.start).seconds < timeout:
            list_elements = self.app.find_elements(By.XPATH, '//android.view.ViewGroup[@content-desc]/android.view.ViewGroup/android.view.ViewGroup')
            return list_elements

    def test_07(self):
        self.app.find_element(AppiumBy.ACCESSIBILITY_ID, "List Demo").click()
        self.app.implicitly_wait(5)
        self.list = self.wait(10)

        assert self.list

    def teardown_method(self):
        self.driver.close_driver()
