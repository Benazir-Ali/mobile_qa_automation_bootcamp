import time
import pytest
import logging
from appium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException


log = logging.getLogger()


class WebCommon:
    def __init__(self, apk_name):
        self.apk_name = apk_name
        self.driver = None

    def init_driver(self, package, activity):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Galaxy API 29'
        desired_caps['app'] = self.apk_name
        desired_caps["appPackage"] = package
        desired_caps["appActivity"] = activity

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        return self.driver

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.quit()


class Test01Android:
    def setup_method(self):
        self.driver_app = WebCommon("/Users/benazir/QTFProjects/theapp.apk")
        self.app = self.driver_app.init_driver("io.cloudgrey.the_app", "io.cloudgrey.the_app.MainActivity")
        self.driver_file = WebCommon("/Users/benazir/QTFProjects/filemanager.apk")
        self.filemanager = self.driver_file.init_driver("com.alphainventor.filemanager", "com.alphainventor.filemanager.activity.MainActivity")
        self.parent = WebElement
        self.child = []

    def open_app(self):
        self.app.implicitly_wait(5)
        self.app.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/continue_button").click()
        self.app.implicitly_wait(5)
        self.app.find_element(AppiumBy.ID, "android:id/button1").click()
        self.app.implicitly_wait(5)

    def find_by_text(self, options, text):
        self.items = self.filemanager.find_elements(AppiumBy.ID, "com.alphainventor.filemanager:id/"+options)
        for i in self.items:
            if i.get_attribute("text") == text:
                return i

    def open_filemanager(self):
        self.filemanager.implicitly_wait(3)
        self.filemanager.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button").click()
        self.filemanager.implicitly_wait(3)
        self.find_by_text("name", "Documents").click()
        self.filemanager.implicitly_wait(3)

    def find_element_by_text(self, text):
        self.text = text
        return self.app.find_element(AppiumBy.ACCESSIBILITY_ID, text)

    def verify(self, text):
        self.text = text
        return self.app.find_element(AppiumBy.ACCESSIBILITY_ID, text)

    def wait_app(self, timeout):
        self.start = datetime.now()
        while (datetime.now() - self.start).seconds < timeout:
            list_elements = self.app.find_elements(By.XPATH, '//android.view.ViewGroup[@content-desc]/android.view.ViewGroup/android.view.ViewGroup')
            return list_elements

    def scroll(self):
        self.app.swipe(0, 1662, 0, 306, 2000)

    def create_folder(self, name):
        self.filemanager.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options').click()
        self.find_by_text("title", "New").click()
        self.filemanager.implicitly_wait(3)
        self.filemanager.find_element(AppiumBy.ID, 'com.alphainventor.filemanager:id/file_name').send_keys(name)
        self.filemanager.implicitly_wait(3)
        self.filemanager.find_element(AppiumBy.ID, 'android:id/button1').click()
        self.filemanager.implicitly_wait(3)

    def delete_folder(self):
        self.filemanager.find_element(AppiumBy.ACCESSIBILITY_ID, "Select").click()
        self.filemanager.implicitly_wait(3)
        self.filemanager.find_element(AppiumBy.ID, 'com.alphainventor.filemanager:id/bottom_menu_delete').click()
        self.filemanager.find_element(AppiumBy.ID, 'android:id/button1').click()

    def rename_folder(self, name):
        self.filemanager.find_element(AppiumBy.ACCESSIBILITY_ID, "Select").click()
        self.filemanager.implicitly_wait(3)
        self.filemanager.find_element(AppiumBy.ID, 'com.alphainventor.filemanager:id/bottom_menu_rename').click()
        self.filemanager.implicitly_wait(3)
        self.filemanager.find_element(AppiumBy.ID, 'com.alphainventor.filemanager:id/file_name').send_keys(name)
        self.filemanager.implicitly_wait(3)
        self.filemanager.find_element(AppiumBy.ID, 'android:id/button1').click()
        self.filemanager.implicitly_wait(3)

    def verify_existence(self, name):
        folders = self.wait_file(10)
        print(folders)
        for i in range(len(folders)):
            if folders[i].get_attribute("text") == name:
                return True
        return False

    def verify_deletion(self):
        try:
            self.filemanager.find_element(AppiumBy.ID, "com.alphainventor.filemanager:id/filename").click()
        except NoSuchElementException:
            return True
        return False

    def wait_file(self, timeout):
        start = time.time()
        folders_list = self.filemanager.find_element(AppiumBy.ID, 'com.alphainventor.filemanager:id/list')
        while (time.time() - start) < timeout:
            elements = folders_list.find_elements(AppiumBy.ID, "com.alphainventor.filemanager:id/filename")
            return elements

    @pytest.mark.parametrize('os', ['android'])
    def test_01(self, os):
        log.info("This is test_01 method")
        log.info("The Operating System is "+os)

    @pytest.mark.xfail(reason="Unable to execute test")
    def test_02(self):
        log.info("This test is expected to fail")

    @pytest.mark.skip(reason="Unable to execute test")
    def test_03(self):
        log.info("This test is to be skipped")

    def test_04(self):
        self.app.implicitly_wait(5)
        self.open_app()
        self.app.implicitly_wait(5)
        self.parent = self.app.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup")
        self.child = self.parent.find_elements(By.XPATH, '//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView')

        assert len(self.child) == 7
        log.info("List size: 7, expected: pass")

    def test_05(self):
        self.app.implicitly_wait(5)
        self.open_app()
        self.app.implicitly_wait(5)
        self.find_element_by_text("List Demo").click()
        self.app.implicitly_wait(5)

        assert self.verify("Altocumulus").is_displayed()
        log.info("Verify that the first item is displayed")

    def test_06(self):
        self.app.implicitly_wait(5)
        self.open_app()
        self.app.implicitly_wait(5)
        self.app.find_element(By.XPATH, '//android.view.ViewGroup[@content-desc="Echo Box"]').click()
        self.app.implicitly_wait(2)
        self.app.find_element(AppiumBy.ACCESSIBILITY_ID, "messageInput").send_keys("Hello World")
        self.app.implicitly_wait(2)
        self.app.find_element(AppiumBy.ACCESSIBILITY_ID, "messageSaveBtn").click()
        self.app.implicitly_wait(2)

        assert self.verify("Hello World").is_displayed()

    def test_07(self):
        self.app.implicitly_wait(5)
        self.open_app()
        self.app.implicitly_wait(5)
        self.app.find_element(AppiumBy.ACCESSIBILITY_ID, "List Demo").click()
        self.app.implicitly_wait(5)
        self.list = self.wait_app(10)

        assert self.list

    def test_08(self):
        self.app.implicitly_wait(5)
        self.open_app()
        self.app.implicitly_wait(3)
        self.app.find_element(AppiumBy.ACCESSIBILITY_ID, "List Demo").click()
        self.app.implicitly_wait(3)
        self.scroll()
        self.app.implicitly_wait(3)

        assert self.verify("Stratus").is_displayed()

    def test_09(self):
        self.open_filemanager()
        self.filemanager.implicitly_wait(3)
        self.create_folder("test_folder")

        assert self.filemanager.find_element(AppiumBy.ACCESSIBILITY_ID, "Select").is_displayed()
        log.info("New Folder detected")

        self.delete_folder()

    def test_10(self):
        self.open_filemanager()
        self.filemanager.implicitly_wait(3)
        self.create_folder("test_folder")
        self.filemanager.implicitly_wait(3)
        self.delete_folder()
        self.filemanager.implicitly_wait(10)

        try:
            self.filemanager.find_element(AppiumBy.ID, "com.alphainventor.filemanager:id/filename")
        except:
            assert True
            log.info("Folder deleted")

    def test_11(self):
        self.open_filemanager()
        self.filemanager.implicitly_wait(3)
        self.create_folder("test_folder")
        self.filemanager.implicitly_wait(3)
        self.rename_folder("secure_folder")
        self.filemanager.implicitly_wait(3)

        name = self.filemanager.find_element(AppiumBy.ID, 'com.alphainventor.filemanager:id/filename').get_attribute("text")

        assert name == "secure_folder"
        log.info("Folder renamed")

    def test_12(self):
        self.open_filemanager()
        self.filemanager.implicitly_wait(3)
        self.create_folder("test_folder")
        self.filemanager.implicitly_wait(3)
        self.delete_folder()
        self.filemanager.implicitly_wait(10)

        assert self.verify_deletion()
        log.info("Exception caught")

    def test_13(self):
        self.open_filemanager()
        self.filemanager.implicitly_wait(3)
        self.create_folder("test_folder")
        self.filemanager.implicitly_wait(3)

        assert self.verify_existence("test_folder")
        log.info("Folder found")

        self.filemanager.implicitly_wait(3)
        self.delete_folder()

    def teardown_method(self):
        self.driver_app.close_driver()
        self.driver_file.close_driver()
