import unittest
import time
from phone_project.test_case.fun_connect_reset import deviceconnect
from appium import webdriver

#定义当前时间点变量
date=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
class TestTab(unittest.TestCase):
    def setUp(self):
        print('start test >>>>>>>>>>>>>>>>')
        deviceconnect(self)
        time.sleep(2)

    def testtabshow(self):
        time.sleep(2)
        element=self.driver.find_element_by_id('com.netease.newsreader.activity:id/bkm')
        self.assertNotEqual(len(element), 0, msg='栏目加载失败')
        print("当前栏目为：",element)
    def testtablist(self):
        i = 3
        for tab in range(6):
            self.driver.swipe(start_x=140, start_y=1480, end_x=140, end_y=440, duration=800)
            time.sleep(2)
            element3 = self.driver.find_elements_by_id('com.netease.newsreader.activity:id/bb1')
            print(element3)
            self.assertNotEqual(len(element3), 0, msg='this page have no more news or  bad request')
        time.sleep(2)
    def tearDown(self):
        self.driver.close_app()
        time.sleep(2)
        self.driver.quit()
        print('test end >>>>>>>>>>>>>>')

if __name__ == "__main__":
        unittest.main()