#sina weibo like robot
#https://m.weibo.cn

import time
from selenium import  webdriver

weiboUrl='https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F'
user='18202700807'#这里是微博账号
password='Cy9805wm'#写入密码

driver = webdriver.Chrome(executable_path="/Users/chy/Desktop/chromedriver")

driver.get(weiboUrl)
time.sleep(5)
driver.find_element_by_id('loginName').clear()
driver.find_element_by_id('loginName').send_keys(user)
driver.find_element_by_id('loginPassword').clear()
driver.find_element_by_id('loginPassword').send_keys(password)
driver.find_element_by_id('loginAction').click()#登陆操作至此完成
time.sleep(4)
#解释下下面两句的作用，这个软件用来给我某个分组用户点赞的，第一句是用来点开我已经有的分组，第二个是点击我其中一个分组，这样才能进入分组进行点赞
#如果你在首页点赞，就不需要下面两句
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/ul/li[1]/span[1]').click()
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div/div[1]/div[2]/ul/li[6]/span').click() #特别关注
#time.sleep(5)

while 1:
    i = 1
    while i <= 10:
        try:
            btn = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div['+str(i)+']/div/div/footer/div[3]')#查找点赞按钮
            i += 1
            if btn.text == '赞':
             time.sleep(5)
             btn.click()
             print("liked")
            else:
             continue
        except:
            print('ERROR')

            driver.refresh()
            time.sleep(2)
            break

    #print("going to refresh in 60s")
    driver.refresh()
    time.sleep(60)#每60秒刷新一次微博内容

driver.close()

