 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import glob
import time
import os
import json
import sys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# get driver execute path

driver_path = r'.\chromedriver'

# 创建存有账号信息的text文件


def create_account():
    account_user = str(input("请输入邮箱/手机号: "))
    account_password = str(input("请输入密码: "))
    # account_num=str(input("请输入“音乐剧云次方净化站”所在分组组号num："))
    account_list = [account_user, "\n", account_password]
    account_alias = input("请为该账号命名一个你容易记住的名字 ")
    account = account_alias + ".txt"
    with open(account, 'w') as f:
        for i in account_list:
            f.write(i)
        f.close()
    return

    # 添加账号信息或退出


def create_or_pass():
    choise = input("是否需要创建新的账号信息？ 需要请输入【Y】，不需要请输入【N】")
    while choise != 'Y' and choise != 'N':
        choise = input("请输入正确指令： 需要请输入【Y】，不需要请输入【N】")
    while choise == 'Y':
        create_account()
        choise = input("是否需要继续添加新的账号信息？ 需要请输入【Y】，不需要请输入【N】")
    return

# Read cookie from local file


def get_cookie_cache(cookieFile):
    cookie_dict = {}
    if os.path.exists(cookieFile):
        with open(cookieFile, 'r') as f:
            for i in json.loads(f.read()):
                if 'name' in i.keys() and 'value' in i.keys():
                    cookie_dict[i['name']] = i['value']
            f.close()
    else:
        return cookie_dict
    return cookie_dict

# Get cookie from server


def login(user, password, account):
    global driver_path
    driver = webdriver.Chrome(executable_path=r''+driver_path)
    weiboUrl = 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F'

    if user.find('@') >= 0:
        print("请注意网页验证提示")
    driver.get(weiboUrl)

    time.sleep(3)
    driver.find_element_by_id('loginName').clear()
    driver.find_element_by_id('loginName').send_keys(user)
    driver.find_element_by_id('loginPassword').clear()
    driver.find_element_by_id('loginPassword').send_keys(password)
    driver.find_element_by_id('loginAction').click()
    time.sleep(5)
    while True:
        if (str(driver.current_url).find('passport.weibo') > 0):
            time.sleep(1)
        else:
            break
    time.sleep(1)
    cookies = driver.get_cookies()

    # driver.get('https://m.weibo.cn/profile/7413113212')

    cookie_dict = {}
    for cookie in cookies:
        if 'name' in cookie.keys() and 'value' in cookie.keys():
            cookie_dict[cookie['name']] = cookie['value']
    cookieFile = account+'_Cookie.txt'
    with open(cookieFile, 'w') as f:
        f.write(json.dumps(cookies))
        f.close()
    return driver


def get_profile(driver, profile):
    while True:
        try:
            driver.find_element_by_xpath(
                '//*[@id="app"]/div[1]/div[1]/div[1]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath(
                '//*[@id="app"]/div[1]/div[1]/div[3]/div[1]/span[2]').click()
            time.sleep(2)
            driver.find_element_by_xpath(
                '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/form/label/input').send_keys(profile)
            driver.find_element_by_xpath(
                '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/form/label/input').send_keys(Keys.ENTER)
            break
        except IndexError:
            time.sleep(3)

    time.sleep(2)
    try:
        driver.find_element_by_xpath(
            '//*[@id="app"]/div[1]/div[1]/div[2]/div/div/div[1]/div/div/header/div/div/a/h3').click()
    except NoSuchElementException:
        print("您尚未关注该用户，请先关注")
        driver.close()
        sys.exit

    time.sleep(2)
    profile_page = str(driver.current_url)
    profile_st = profile_page.find('u/')
    profile_ed = profile_page.find('?')
    profile_path = profile_page[profile_st+2:profile_ed]

    with open('path_profile.txt', 'w') as f:
        f.write(profile_path)
        f.close()
    return driver, profile_path


def go_to_target(cookieFile, user, password, account):
    global driver_path
    cookies = get_cookie_cache(cookieFile)
    if not cookies:
        log = login(user, password, account)
        driver = log
        return driver
    else:
        # Login once to delete cookie first
        driver = webdriver.Chrome(executable_path=r''+driver_path)
        driver.get('https://m.weibo.cn/')
        time.sleep(1)
        driver.delete_all_cookies()
        # Add new cookie and login to target page
        for i, j in cookies.items():
            driver.add_cookie({'name': i, 'value': j})
        time.sleep(1)
        driver.get('https://m.weibo.cn/')
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
        if str(driver.current_url).find('m.weibo.cn/login') > 0:
            driver.close()
            log = login(user, password, account)
            driver = log
    return driver


def file_search():
    file_list = glob.glob('*.txt')
    files = []
    for i in file_list:
        if i.find('_') == -1:
            i = i.split('.')[0]
            files.append(i)
    return files


files = file_search()
# select account
account = input(f"请选择登入账号,您现在有以下账号：{files} \n添加新账号请输入【添加账号】 ")
if account == "添加账号":
    create_or_pass()
    files = file_search()
    account = input(f"请选择登入账号,您现在有以下账号：{files}\n 添加新账号请输入【添加账号】 ")

accountFile = account+'.txt'

# verify account
while not os.path.exists(accountFile):
    select = input(
        "你没有该账号信息，请选择其他账号或新建账号信息，是否选择其他账号？ \n选择其他账号请输入【Y】，选择新建账号信息请输入【N】")
    while select != "Y" and select != "N":
        select = input("请输入正确指令： \n选择其他账号请输入【Y】，选择新建账号信息请输入【N】")
    if select == "Y":
        account = input("请选择登入账号 ")
        accountFile = account+'.txt'
    else:
        create_account()
        account = input("请选择登入账号 ")
        accountFile = account+'.txt'

# get account info
if os.path.exists(accountFile):
    with open(accountFile, 'r') as f:
        [user, password] = f.read().splitlines()
        f.close()
cookieFile = account+'_Cookie.txt'

driver = go_to_target(cookieFile, user, password, account)

# verify profile path exist
if os.path.exists('path_profile.txt'):
    with open('path_profile.txt', 'r') as f:
        profile_path = f.read()
        f.close()
else:
    profile = input(
        "请输入净化组账号名称，净化组有以下四个账号：\n【音乐剧云次方净化站】【云云净化小助手1号】\n【云云净化小助手2号】【云云净化小助手3号】")
    main = get_profile(driver, profile)
    profile_path = main[1]
    driver = main[0]

    # verify if the path belongs to cloud
    profile_list = ['5521179668', '7413113212', '7330084630', '7344774254']
    while True:
        if profile_path not in profile_list:
            profile = input(
                "请输入净化组账号，净化组有以下四个账号：\n【音乐剧云次方净化站】【云云净化小助手1号】\n【云云净化小助手2号】【云云净化小助手3号】")
            main = get_profile(driver, profile)
            profile_path = main[1]
            driver = main[0]
        else:
            break

target_url = 'https://m.weibo.cn/profile/'+profile_path

# 处理净化组挂号情况
driver.get(target_url)
time.sleep(2)
try:
    driver.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/div/h3/span')
except NoSuchElementException:
    profile = input(
        '该小净已挂，请输入其他账号，净化组有以下四个账号：\n【音乐剧云次方净化站】【云云净化小助手1号】\n【云云净化小助手2号】【云云净化小助手3号】: ')
    driver.get('https://m.weibo.cn/')
    main = get_profile(driver, profile)
    driver = main[0]
    profile_path = main[1]
    target_url = 'https://m.weibo.cn/profile/'+profile_path
    driver.get(target_url)

k = int(input("请输入第__条卡黑帖："))
print("【用户输入完毕】")
btn = driver.find_element_by_xpath(
    '//*[@id="app"]/div/'+'div['+str(k+1)+']/div/div/footer/div[2]')  # 查找评论按钮
btn.click()
st = time.time()

time.sleep(1)
test = driver.find_elements_by_class_name("m-img-box")
verify = test[0].get_attribute('href')
verify
l = len(verify)

if verify[(l-10):l] != profile_path:  # 5521179668
    print("---Identity Error---")
    driver.close()
    sys.exit()
time.sleep(3)
links = driver.find_elements_by_link_text("网页链接")
length = len(links)

print("待处理数量：", length)
curUrl = driver.current_url
driver.delete_all_cookies()


for i in range(0, length):
    st = time.time()
    while(time.time()-st < 30):
        links = driver.find_elements_by_link_text("网页链接")
        if len(links) == length:
            break
    else:
        print("---Link Error---")
        driver.close()
        sys.exit()
    target = links[i]
    driver.execute_script("arguments[0].scrollIntoView();", target)
    driver.execute_script('window.scrollBy(0,-100)')
    links[i].click()
    time.sleep(3)

    # 处理跳转登录界面
    if str(driver.current_url).find("weibo.com/login") > 0:
        # 邮箱登录大概率验证，直接扫码
        if user.find("@") > 0:
            print("请注意页面操作")
            driver.find_element_by_xpath(
                '//*[@id="pl_login_form"]/div/div[1]/div/a[2]').click()
        # 手机登录先输入信息
        else:
            driver.find_element_by_id('loginname').clear()
            driver.find_element_by_id('loginname').send_keys(user)
            driver.find_element_by_xpath(
                '//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').clear()
            driver.find_element_by_xpath(
                '//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys(password)
            driver.find_element_by_xpath(
                '//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
            time.sleep(10)
            # 等待时间过长大概率需要验证，直接扫码
            if str(driver.current_url).find("weibo.com/login") > 0:
                driver.find_element_by_xpath(
                    '//*[@id="pl_login_form"]/div/div[1]/div/a[2]').click()
                while str(driver.current_url).find("weibo.com/login") > 0:
                    time.sleep(3)
    st = time.time()
    while(time.time()-st < 60):
        tab1 = driver.find_elements_by_link_text("有害信息")
        if len(tab1) != 0:
            break
#         else:
#            print("---Type Error---")
#            driver.close()
#            sys.exit()
    if len(tab1) == 0:
        time.sleep(0.5)
        driver.get(curUrl)
        continue
    tab1[0].click()
    driver.execute_script('window.scrollBy(0,100)')
    tab2 = driver.find_element_by_link_text("其他有害信息")
    tab2.click()
    driver.execute_script('window.scrollBy(0,200)')
    time.sleep(0.5)

    # 点击选框
    check = driver.find_elements_by_class_name('inp_chk')
    check[len(check)-1].click()
    time.sleep(0.2)
    submit = driver.find_element_by_link_text("提交")
    submit.click()
    time.sleep(0.5)
    driver.get(curUrl)

    print('\r'+str(int(((i+1)*100)/length))+'%', end='')
    time.sleep(3)


print('\nDONE')

driver.close()
