from appium.webdriver.common.appiumby import AppiumBy
from driver import WebCommon
import logging

logging.basicConfig(filename="test_05.log")
log = logging.getLogger()


class Test05Android:
    def setup_method(self):
        self.driver = WebCommon("/Users/benazir/QTFProjects/theapp.apk")
        self.app = self.driver.init_driver()

    def find_element_by_text(self, text):
        self.text = text
        return self.app.find_element(AppiumBy.ACCESSIBILITY_ID, text)

    def verify(self, text):
        self.text = text
        return self.app.find_element(AppiumBy.ACCESSIBILITY_ID, text)

    def test_05(self):
        self.find_element_by_text("List Demo").click()
        self.app.implicitly_wait(5)

        log.info("Verify that the first item is displayed")
        assert self.verify("Altocumulus").is_displayed()

    def teardown_method(self):
        self.driver.close_driver()
