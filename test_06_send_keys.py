from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from driver import WebCommon


class Test06Android:
    def setup_method(self):
        self.driver = WebCommon("/Users/benazir/QTFProjects/theapp.apk")
        self.app = self.driver.init_driver()

    def verify(self, text):
        self.text = text
        return self.app.find_element(AppiumBy.ACCESSIBILITY_ID, text)

    def test_06(self):
        self.app.find_element(By.XPATH, '//android.view.ViewGroup[@content-desc="Echo Box"]').click()
        self.app.implicitly_wait(2)
        self.app.find_element(AppiumBy.ACCESSIBILITY_ID, "messageInput").send_keys("Hello World")
        self.app.implicitly_wait(2)
        self.app.find_element(AppiumBy.ACCESSIBILITY_ID, "messageSaveBtn").click()
        self.app.implicitly_wait(2)

        assert self.verify("Hello World").is_displayed()

    def teardown_method(self):
        self.driver.close_driver()



