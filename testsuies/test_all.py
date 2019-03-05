# from  testsuies.test_luntan2 import test_baidusearch2
# from  testsuies.test_luntan_search import test_baidusearch
# from testsuies.test_luntan3 import test_baidusearch3
# from testsuies.test_luntan4 import test_baidusearch4
import unittest
import HTMLTestRunner
import os
import sys
sys.path.append("E:\\Discuz\\")
dir='./'
# suite=unittest.TestSuite()
# suite.addTest(unittest.makeSuite(test_baidusearch))
# suite.addTest(unittest.makeSuite(test_baidusearch2))
# suite.addTest(unittest.makeSuite(test_baidusearch3))
# suite.addTest(unittest.makeSuite(test_baidusearch4))
sut=unittest.TestLoader().discover(dir,pattern='test_luntan*')

if __name__=="__main__":

    html_report=r"e:\Discuz\report\result.html"
    fp=open(html_report,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="测试报告",description="用例执行情况")
    runner.run(sut)