from appium import webdriver


class WebCommon:
    def __init__(self, apk_name):
        self.apk_name = apk_name
        self.driver = None

    def init_driver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10.0'
        desired_caps['deviceName'] = 'Galaxy API 29'
        desired_caps['app'] = 'apk_name'
        desired_caps['appActivity'] = '.Settings'
        desired_caps['appPackage'] = 'com.android.settings'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        return self.driver

    def get_driver(self):
        self.driver = self.init_driver()

    def close_driver(self):
        self.driver.quit()
