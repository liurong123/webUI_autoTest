import unittest
import time
import HTMLTestRunner
from testsuies.base_testcase import Test_basecase
from pageobjects.luntan_indexpage import *
class test_baidusearch(Test_basecase):
   def test_luntan(self):
      index=IndexPage(self.driver)
      # index.get("http://127.0.0.1/forum.php")
      index.Login("admin","123456")
      time.sleep(5)
      faitie=FaTie(self.driver)
      faitie.fatie("标题","正文")
      time.sleep(5)
      huitie=HuiTie(self.driver)
      huitie.huitie("回帖")
      time.sleep(5)
      logout=TuiChu(self.driver)
      logout.tuichu()


if __name__=="__main__":
   # html_report = r"e:\Discuz\report\result.html"
   # fp = open(html_report, 'wb')
   # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="测试报告", description="用例执行情况")
   # runner.run(unittest.main())
   unittest.main()
