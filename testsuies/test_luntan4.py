import unittest
import time
import HTMLTestRunner
from testsuies.base_testcase import Test_basecase
from pageobjects.luntan_indexpage import *
class test_baidusearch4(Test_basecase):
   def test_luntan4(self):
      index = IndexPage(self.driver)
      index.Login("admin", "123456")
      time.sleep(5)
      faqitoupiao=FaQiTouPiao(self.driver)
      faqitoupiao.faqitoupiao("发起投票", "选项1","选项2")
      time.sleep(5)
      toupia=TouPiao(self.driver)
      toupia.toupiao()
      time.sleep(5)
      huoqu=HuoQu(self.driver)
      huoqu.houqu()
      time.sleep(5)
      logout=TuiChu(self.driver)
      logout.tuichu()


if __name__=="__main__":
   unittest.main()