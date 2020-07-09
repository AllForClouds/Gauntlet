import time
import sys
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
driver.find_element_by_id('loginAction').click()

#若邮箱登录，需要经过人工验证
#if user.find('@')>=0:
    #time.sleep(10)

st=time.time()
while(time.time()-st<10):
    focus=driver.find_elements_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/ul/li[1]/span[1]')
    if len(focus)!=0:
        break
else:
    print("---Run Error--")
focus[0].click()
time.sleep(1)
num=int(input("请输入“音乐剧云次方净化站”所在分组组号num：")) 
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div/div[1]/div[2]/ul/li['+str(num)+']/span').click() #特别关注
time.sleep(1)
k=int(input("请输入第__条卡黑帖：")) 
btn = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/'+'div['+str(k)+']/div/div/footer/div[2]')#查找评论按钮(倒数第二个div[1]可换)
btn.click()
st=time.time()
while(time.time()-st<10):
    ids=driver.find_elements_by_link_text("音乐剧云次方净化站")
    if len(ids)!=0:
            break
else:
    print("---Identity Error---")
    driver.close()
    sys.exit()
while(time.time()-st<10):
    links=driver.find_elements_by_link_text("网页链接")
    if len(links)!=0:
        break
length=len(links)
print("待处理数量：",length)
for i in range(0,length):
    st=time.time()
    while(time.time()-st<10):
        links=driver.find_elements_by_link_text("网页链接")
        if len(links)!=0:
            break
    target=links[i]
    driver.execute_script("arguments[0].scrollIntoView();", target)
    driver.execute_script('window.scrollBy(0,-100)')
    try:
        links[i].click()
    except:
        print("---Link Error---")
    st=time.time()
    while(time.time()-st<10):
        tab1=driver.find_elements_by_link_text("有害信息")
        if len(tab1)!=0:
            break
    try:
        tab1[0].click()
    except:
        print("---Type Error---")
        driver.close()
        sys.exit()
    tab2=driver.find_element_by_link_text("其他有害信息")
    tab2.click()
    driver.execute_script('window.scrollBy(0,300)')
    time.sleep(0.5)
    #点击选框
    check = driver.find_element_by_class_name('inp_chk')
    check.click()
    submit=driver.find_element_by_link_text("提交")
    submit.click()
    driver.back()
    print('\r'+str(int(((i+1)*100)/length))+'%', end='')
print('\nDONE')

