from appium.webdriver.common.appiumby import AppiumBy
from driver import WebCommon


class Test08Android:
    def setup_method(self):
        self.driver = WebCommon("/Users/benazir/QTFProjects/theapp.apk")
        self.app = self.driver.init_driver()

    def verify(self, text):
        self.text = text
        return self.app.find_element(AppiumBy.ACCESSIBILITY_ID, text)

    def scroll(self):
        self.app.swipe(0, 1662, 0, 306, 2000)

    def test_08(self):
        self.app.find_element(AppiumBy.ACCESSIBILITY_ID, "List Demo").click()
        self.scroll()
        self.app.implicitly_wait(3)

        assert self.verify("Stratus").is_displayed()

    def teardown_method(self):
        self.driver.close_driver()
