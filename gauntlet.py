#sina weibo like robot
#https://m.weibo.cn

import time
from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains

weiboUrl='https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F'
user=input("请输入邮箱/手机号:")
password=input("请输入密码:")

#此处改为chromedriver本地位置
driver = webdriver.Chrome(executable_path="/Users/chy/Desktop/chromedriver")
driver.get(weiboUrl)
time.sleep(3)
driver.find_element_by_id('loginName').clear()
driver.find_element_by_id('loginName').send_keys(user)
driver.find_element_by_id('loginPassword').clear()
driver.find_element_by_id('loginPassword').send_keys(password)
driver.find_element_by_id('loginAction').click()#登陆操作至此完成
time.sleep(2)
#解释下下面两句的作用，这个软件用来给我某个分组用户点赞的，第一句是用来点开我已经有的分组，第二个是点击我其中一个分组，这样才能进入分组进行点赞
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/ul/li[1]/span[1]').click()
time.sleep(2)
#此行li[6]中6改为num
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div/div[1]/div[2]/ul/li[6]/span').click() #特别关注
time.sleep(5)

btn = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div/footer/div[2]')#查找评论按钮(倒数第二个div[1]可换)
time.sleep(1)
btn.click()

time.sleep(2)
links=driver.find_elements_by_link_text("网页链接")
length=len(links)
print(length)
for link in links:
    driver.execute_script('window.scrollBy(0,500)')#向下滚动
    time.sleep(2)
    link.click()
    time.sleep(3)
    tab1=driver.find_element_by_link_text("有害信息")
    tab1.click()
    time.sleep(2)
    tab2=driver.find_element_by_link_text("其他有害信息")
    tab2.click()
    driver.execute_script('window.scrollBy(0,300)')#向下滚动
    time.sleep(3)
    check = driver.find_element_by_class_name('inp_chk')
    #直接点击选框
    check.click()
    time.sleep(2)
    #勾选后，判断选框状态
    submit=driver.find_element_by_link_text("提交")
    submit.click()
    driver.back()

