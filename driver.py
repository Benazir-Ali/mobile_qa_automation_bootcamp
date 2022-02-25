from appium import webdriver


class WebCommon:
    def capabilities (self):
        desired_caps = {'platformName': 'Android', 'deviceName': 'Tester', 'appPackage': 'com.google.android.youtube',
                        'appActivity': 'com.google.android.apps.youtube.app.application.Shell$HomeActivity',
                        'noReset': 'true', 'forceMjsonwp': 'true'}
        return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)