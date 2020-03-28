from appium import webdriver


def init_driver():
    # server 启动参数
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.164.101:5555'
    # app信息
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'
    # 中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 声明对象
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
