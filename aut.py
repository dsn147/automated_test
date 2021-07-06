'''
    python自动化刷抖音
'''
from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver
from appium import webdriver

import time

server = "http://localhost:4723/wd/hub"
param = {
			  "deviceName": "20a8168a",
			  "platformName": "Android",
			  "platformVersion": "10",
			  "appPackage": "com.ss.android.ugc.aweme",
			  "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity"
}
driver = webdriver.Remote(server,param)


time.sleep(30)
driver.swipe(505,1751,642,617,300)
while True:
	driver.swipe(505, 1751, 642, 617, 300)
	time.sleep(10)


# time.sleep(1000)

# driver.quit()






















