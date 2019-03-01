import unittest
from framework.browser_engine import BrowerEngine
from selenium import webdriver
class Test_basecase(unittest.TestCase):
    def setUp(self):
        self.browerengine=BrowerEngine()
        self.driver=self.browerengine.open_driver()
        # self.driver=webdriver.Chrome("../tools/chromedriver.exe")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(6)
    def tearDown(self):
        self.browerengine.quit_browser()
        print("结束")
        # self.driver.guanbi()


