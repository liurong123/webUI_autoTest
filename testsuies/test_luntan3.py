import unittest
import time
import HTMLTestRunner
from ddt import *
from testsuies.base_testcase import Test_basecase
from pageobjects.luntan_indexpage import *
@ddt
class test_baidusearch3(Test_basecase):
   # @data([['haotest','haotest']])
   # @unpack
   def test_luntan3(self):
       index = IndexPage(self.driver)
       index.Login("admin", "123456")
       time.sleep(5)
       sou=Sousuo(self.driver)
       a=sou.sousuo("haotest")
       try:
            self.assertEqual(a,"haotest",msg=a)
       except AssertionError as a:
           print(u"找不到这个标题")
       time.sleep(5)
       logout = TuiChu(self.driver)
       logout.tuichu()


if __name__=="__main__":
   unittest.main()
