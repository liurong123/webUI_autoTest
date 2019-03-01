from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
logger=Logger(logger='Base').getlog()
class Base(object):
    def __init__(self,driver):
        self.driver=driver
    def close(self):
        self.driver.close()
    def back(self):
        self.driver.back()
    def forward(self):
        self.driver.forward()
    def get(self,url):
        self.driver.get(url)
    def quit_browser(self):
        pass
    def find_element(self,*element):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(element))
            return self.driver.find_element(*element)
            # logger.error("找到页面元素")
        except:
            logger.error("%s未找到页面%s元素"%(self,element))
    def sendkeys(self,text,*element):
        ele=self.find_element(*element)
        ele.send_keys(text)
        logger.info("输入内容")
    def clik(self,*element):
        ele=self.find_element(*element)
        ele.click()
    def clear(self,*element):
        ele=self.find_element(*element)
        ele.clear()
    def guanbi(self):
        self.driver.quit()
    def jihuo(self):
        self.driver.switch_to.window(self.driver.current_window_handle)
    def switch_to(self,*element):
        ele=self.find_element(*element)
        self.driver.switch_to.frame(ele)
    def jh(self,x):
        self.driver.switch_to.window(self.driver.window_handles[x])
    def text(self,*element):
        ele=self.find_element(*element)
        return  ele.text



