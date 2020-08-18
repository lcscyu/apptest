import unittest
import HTMLTestRunner
import time
from phone_project.test_case.fun_send_mail import sendreport
def suite():
    testsuite=unittest.TestSuite()
    #define the directory to find testcases
    test_dir='E:\\PythonCode\\phone_project\\test_case'
    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern='test_*.py',
                                                   top_level_dir=None)
    #discover 筛选的用例加入到循环套件
    for test_suite in discover:
        for test_case in test_suite:
            testsuite.addTest(test_case)
            print(testsuite)
    return testsuite

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filename="E:\\PythonCode\\phone_project\\result\\" + now + "HtmlReport.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'TestReport',
                                           description=u'the details of testcases')
    runner.run(suite())
    fp.close()
    time.sleep(80)
    sendReport()
