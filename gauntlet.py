#sina weibo like robot
#https://m.weibo.cn

import time
from selenium import  webdriver

weiboUrl='https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F'
user=''#这里是微博账号
password=''#写入密码

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

#此行li[6]中6改为num
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div/div[1]/div[2]/ul/li[6]/span').click() #特别关注
time.sleep(8)

btn = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div/footer/div[2]')#查找评论按钮(倒数第二个div[1]可换)
time.sleep(1)
btn.click()


links=driver.find_elements_by_link_text("网页链接")
length=len(links)
for i in range(0,length):
    link = links[i]
    link.click()
    tab1=driver.find_elements_by_link_text("有害信息")
    tab1.click()
    tab2=driver.find_elements_by_link_text("其他有害信息")
    tab2.click()
    asser = driver.find_element_by_id("readRoleInput").is_selected()  
    #直接点击选框
    driver.find_element_by_id("readRoleInput").click()
    sleep(2)
    #勾选后，判断选框状态
    asser1 = driver.find_element_by_id("readRoleInput").is_selected()
    print(asser1)
    submit=driver.find_elements_by_link_text("提交")
    submit.click()
    print(i)
    driver.back()

