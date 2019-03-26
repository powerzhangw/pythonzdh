# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os, traceback


# 定义函数，专门用来打开浏览器
def openbrowser(b='chrome', dpath='../lib/', t=10):
    if b == 'chrome':
        dpath += 'chromedriver'
        # 创建一个ChromeOptions的对象
        option = webdriver.ChromeOptions()
        # 去掉提示条的配置
        option.add_argument('disable-infobars')
        # 获取用目录
        try:
            # 异常处理，如果获取到，就使用获取到路径
            userdir = os.environ['USERPROFILE']
        except Exception as e:
            # 如果没有获取到，就使用默认的Administrator路径
            # 打印异常信息
            # traceback.print_exc()
            userdir = 'C:\\Users\\Administrator'

        userdir += '\\AppData\\Local\\Google\\Chrome\\User Data'
        userdir = '--user-data-dir=' + userdir
        # 添加用户目录
        option.add_argument(userdir)
        # 调用谷歌浏览器
        driver = webdriver.Chrome(executable_path=dpath, options=option)
        # 设置默认等待时间
        driver.implicitly_wait(t)
        return driver

    if b == 'ff':
        dpath += 'geckodriver'
        driver = webdriver.Firefox(executable_path=dpath)
        # 设置默认等待时间
        driver.implicitly_wait(t)
        return driver

    if b == 'ie':
        dpath += 'IEDriverServer'
        driver = webdriver.Ie(executable_path=dpath)
        # 设置默认等待时间
        driver.implicitly_wait(t)
        return driver


class Web:
    # 构造函数，用来创建实例变量，初始化一些代码
    def __init__(self):
        # 初始化浏览器对象的实例变量
        # 实例变量用来保存打开的浏览器
        self.driver = None

    # 定义函数，专门用来打开浏览器
    def openbrowser(self, b='cc', dpath='../lib/', t=10):
        if b == 'cc':
            dpath += 'chromedriver'
            # 创建一个ChromeOptions的对象
            option = webdriver.ChromeOptions()
            # 去掉提示条的配置
            option.add_argument('disable-infobars')
            # 获取用目录
            try:
                # 异常处理，如果获取到，就使用获取到路径
                userdir = os.environ['USERPROFILE']
            except Exception as e:
                # 如果没有获取到，就使用默认的Administrator路径
                # 打印异常信息
                # traceback.print_exc()
                userdir = 'C:\\Users\\Administrator'

            userdir += '\\AppData\\Local\\Google\\Chrome\\User Data'
            userdir = '--user-data-dir=' + userdir
            # 添加用户目录
            option.add_argument(userdir)
            # 调用谷歌浏览器
            self.driver = webdriver.Chrome(executable_path=dpath, options=option)
            # 设置默认等待时间
            self.driver.implicitly_wait(t)
            return self.driver

        if b == 'ff':
            dpath += 'geckodriver'
            self.driver = webdriver.Firefox(executable_path=dpath)
            # 设置默认等待时间
            self.driver.implicitly_wait(t)
            return self.driver

        if b == 'ie':
            dpath += 'IEDriverServer'
            self.driver = webdriver.Ie(executable_path=dpath)
            # 设置默认等待时间
            self.driver.implicitly_wait(t)
            return self.driver


# main入口
if __name__ == '__main__':
    # driver = webdriver.Firefox(executable_path='../lib/geckodriver')
    # driver.get('http://www.baidu.com')

    # driver = webdriver.Ie(executable_path='../lib/IEDriverServer')
    web = Web()
    driver = web.openbrowser()
    driver.get('http://112.74.191.10:8000/')
    # 找到这个元素
    ele = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/a[1]')
    # 再点击这个元素
    ele.click()

    # 登录
    ele = driver.find_element_by_id('username')
    ele.send_keys("13800138006")

    ele = driver.find_element_by_css_selector('#password')
    ele.send_keys('123456')

    ele = driver.find_element_by_xpath('//*[@id="verify_code"]')
    ele.send_keys('111111')

    ele = driver.find_element_by_css_selector('#loginform > div > div.login_bnt > a')
    ele.click()

    # 搜索
    ele = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/ul/li[1]/a')
    ele.click()

    ele = driver.find_element_by_xpath('//*[@id="q"]')
    ele.send_keys('手机')

    ele = driver.find_element_by_xpath('//*[@id="searchForm"]/button')
    ele.click()

    # 移动到元素
    ele = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/ul/li[10]/div/div[5]/div[2]/a')
    actions = ActionChains(driver)
    actions.move_to_element(ele).perform()
    # 点加购物车
    ele.click()

    # 切换iframe
    # 校验添加成功
    ele = driver.find_element_by_xpath('//*[@id="layui-layer-iframe1"]')
    # 三种定位，id，name，元素
    driver.switch_to.frame(ele)

    ele = driver.find_element_by_xpath('//*[@id="addCartBox"]/div[1]/div/span')
    print(ele.text)

    # 切出iframe
    driver.switch_to.default_content()
    ele = driver.find_element_by_xpath('//*[@id="layui-layer1"]/span/a')
    ele.click()

    # 滚回购物车按钮
    ele = driver.find_element_by_xpath('//*[@id="hd-my-cart"]/a/div')
    actions.move_to_element(ele).perform()
    ele.click()

    ele = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div[2]/div[1]/a')
    ele.click()

    ele = driver.find_element_by_xpath('/html/body/div[14]/div/button')
    ele.click()
