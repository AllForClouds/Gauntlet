import time
from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains

weiboUrl='https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F'
user=input("请输入邮箱/手机号:")
password=input("请输入密码:")

#此处改为chromedriver的本地位置
driver = webdriver.Chrome(executable_path="/Users/chy/Desktop/chromedriver")

#全屏（如需要全屏，将下一行取消注释即可）
#driver.maximize_window()

driver.get(weiboUrl)
time.sleep(5)
driver.find_element_by_id('loginName').clear()
driver.find_element_by_id('loginName').send_keys(user)
driver.find_element_by_id('loginPassword').clear()
driver.find_element_by_id('loginPassword').send_keys(password)
driver.find_element_by_id('loginAction').click()#登陆操作至此完成
time.sleep(2)

#若邮箱登录，需要经过人工验证
if user.find('@')>=0:
    time.sleep(10)

#点开已有分组
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/ul/li[1]/span[1]').click()
time.sleep(2)

#输入组号，如默认中特别关注组号为6
num=int(input("请输入“音乐剧云次方净化站”所在分组组号num：")) 
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div/div[1]/div[2]/ul/li['+str(num)+']/span').click() #特别关注
time.sleep(5)

k=int(input("请输入第__条卡黑帖：")) #选择第k条进行卡黑操作
btn = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/'+'div['+str(k)+']/div/div/footer/div[2]')#查找评论按钮(倒数第二个div[1]可换)
time.sleep(1)
btn.click()

time.sleep(2)
links=driver.find_elements_by_link_text("网页链接")
length=len(links)
print("待处理数量：")
print(length)
for i in range(0,length):
    links=driver.find_elements_by_link_text("网页链接")
    driver.execute_script('window.scrollBy(0,500)')#向下滚动500
    time.sleep(2)
    links[i].click()
    time.sleep(3)
    tab1=driver.find_element_by_link_text("有害信息")
    tab1.click()
    time.sleep(2)
    tab2=driver.find_element_by_link_text("其他有害信息")
    tab2.click()
    driver.execute_script('window.scrollBy(0,300)')#向下滚动300
    time.sleep(3)
    #点击选框
    check = driver.find_element_by_class_name('inp_chk')
    check.click()
    time.sleep(2)
    submit=driver.find_element_by_link_text("提交")
    submit.click()
    driver.back()
    time.sleep(2)
    print('\r'+str(int((i*100)/length))+'%', end='')
print('DONE')

