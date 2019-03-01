import os.path
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger
logger=Logger(logger="BrowerEngine").getlog()
class BrowerEngine(object):
    dir=os.path.dirname(os.path.abspath("."))
    chrom_driver_path=dir+"/tools/chromedriver.exe"
    ie_driver_path=dir+"/tools/IBDriver.exe"
    firefox_driver=dir+"/tools/geckodriver.exe"
    def open_driver(self):
        config=ConfigParser()
        file_path=os.path.dirname(os.path.abspath("."))+"/config/config.ini"
        config.read(file_path)
        browser=config.get("browserType","browserName")
        logger.info("读取浏览器成功")
        url=config.get("testServer",'URL')
        logger.info("找到URL:%s"%url)
        if browser=="Firefox":
            logger.info("浏览器为火狐")
        elif browser=="Chrom":
            self.driver=webdriver.Chrome(self.chrom_driver_path)
            logger.info("浏览器为谷歌")
        else:
            self.driver=webdriver.Ie(self.ie_driver_path)
            logger.info("浏览器为IE")
        self.driver.get(url)
        logger.info("打开浏览器%s"%url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return  self.driver
    def quit_browser(self):
        logger.info("现在关闭浏览器")
        self.driver.quit()