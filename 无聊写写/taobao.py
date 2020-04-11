# -*- coding: utf-8 -*-
import os
import datetime
import time
from os import path
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 定义一个taobao类
class taobao_infos:

    # 对象初始化
    def __init__(self):
        taobao_url = 'https://login.taobao.com/member/login.jhtml'
        self.url = taobao_url

        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 不加载图片,加快访问速度
        options.add_experimental_option('excludeSwitches',
                                        ['enable-automation'])  # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium

        self.browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)
        self.wait = WebDriverWait(self.browser, 10)  # 超时时长为10s

    # 登录淘宝
    def login(self):
        # 打开网页
        self.browser.get(self.url)

        # 等待 密码登录选项 出现
        password_login = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.qrcode-login > .login-links > .forget-pwd')))
        password_login.click()

        # 等待 微博登录选项 出现
        weibo_login = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.weibo-login')))
        weibo_login.click()

        # 等待 微博账号 出现
        weibo_user = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.username > .W_input')))
        weibo_user.send_keys(weibo_username)

        # 等待 微博密码 出现
        weibo_pwd = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.password > .W_input')))
        weibo_pwd.send_keys(weibo_password)

        # 等待 登录按钮 出现
        submit = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn_tip > a > span')))
        submit.click()

        # 直到获取到淘宝会员昵称才能确定是登录成功
        taobao_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                      '.site-nav-bd > ul.site-nav-bd-l > li#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-user > a.site-nav-login-info-nick ')))
        # 输出淘宝昵称
        now = datetime.datetime.now()
        print('登陆成功:', now.strftime('%Y-%m-%d %H:%M:%S'))
        print('淘宝昵称', taobao_name.text)

    def cart(self):
        self.browser.get('https://cart.taobao.com/cart.htm')
        now = datetime.datetime.now()
        print('成功进入购物车:', now.strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(1)

    def buy(self, times, choose):
        #对相应店铺商品进行全选
        time.sleep(1)

        while True:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            #webdriver.Chrome(executable_path=chromedriver_path).find_element_by_xpath('//*[@id="J_Item_1428677233013"]/ul/li[1]/div/div/label').click()
            #对比时间，时间到的话就点击结算
            if now > times:
                while True:
                    # 等待 商店选项 出现
                    try:
                        if self.browser.find_element_by_xpath(choose):
                            self.browser.find_element_by_xpath(choose).click()
                            title = self.browser.title

                            print("选择商品成功")
                            break
                    except:
                        print("找不到商品")

                # 点击结算按钮
            while True:
                try:
                    if self.browser.find_element_by_id("J_Go"):
                        self.browser.find_element_by_id("J_Go").click()
                        title = self.browser.title
                        print("提交成功，进入确认订单模式")
                        break

                except:
                    print("提交不成功")


            while True:
                    try:
                        if self.browser.find_element_by_link_text('提交订单'):
                            self.browser.find_element_by_link_text('提交订单').click()
                            print("确认订单成功，进入付款模式")
                            break
                    except:
                        print("再次尝试确认订单")
            time.sleep(0.01)

            break


# 使用教程：
# 1.下载chrome浏览器:https://www.google.com/chrome/
# 2.查看chrome浏览器的版本号，下载对应版本号的chromedriver驱动:http://chromedriver.storage.googleapis.com/index.html
# 3.填写chromedriver的绝对路径
# 4.执行命令pip install selenium
# 5.打开https://account.weibo.com/set/bindsns/bindtaobao并通过微博绑定淘宝账号密码


if __name__ == "__main__":
    chromedriver_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"  # 改成你的chromedriver的完整路径地址
    weibo_username = "————————"  # 改成你的微博账号
    weibo_password = "————————"  # 改成你的微博密码

    print("吼吼吼，要开始剁手了么")
    choose = input("请输入店铺代码XPATH，格式如（//div[@id='J_Order_s_916243692_1']/div/div/div/label):\n")
    times = input("请输入抢购时间，格式如(2019-08-08 11:20:00.000000):\n")

    a = taobao_infos()
    a.login()  # 登录
    a.cart()    #进入购物车
    a.buy(times, choose)