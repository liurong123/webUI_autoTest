import unittest
import time
import HTMLTestRunner
from testsuies.base_testcase import Test_basecase
from pageobjects.luntan_indexpage import *
class test_baidusearch2(Test_basecase):
   def test_luntan2(self):
      index=IndexPage(self.driver)
      index.Login("admin", "123456")
      time.sleep(5)
      delete=Delete(self.driver)
      delete.delete()
      time.sleep(5)
      add=AddNewModule(self.driver)
      add.addNewModule("新论坛名称")
      time.sleep(5)
      logout = TuiChu(self.driver)
      logout.tuichu()
      time.sleep(5)
      logout.tuichu()
      index=IndexPage(self.driver)
      index.Login("root","root123")
      time.sleep(5)
      faitie=FaTie(self.driver)
      faitie.newfatie("新模块标题","新模块正文",'新论坛名称')
      time.sleep(3)
      huitie=HuiTie(self.driver)
      huitie.huitie("新模块回帖")
      time.sleep(3)
      logout=TuiChu(self.driver)
      logout.tuichu()


if __name__=="__main__":
   unittest.main()