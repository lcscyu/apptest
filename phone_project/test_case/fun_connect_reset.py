# coding=utf-8
from appium import webdriver
import time

def deviceconnect(self):
    caps = {
        'platformName': 'Android',
        'platformVersion': '7.0',
        'deviceName': 'HMK7N17315000689',
        'appPackage': 'com.netease.newsreader',
        'appActivity': 'com.netease.newsreader.activity'
        }
    self.driver=webdriver.Remote('http://XXXX:4723/wd/hub',caps)
    time.sleep(10)

