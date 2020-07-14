import time
import sys
from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains

weiboUrl='https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F'

user=input("请输入邮箱/手机号:")
password=input("请输入密码:")
num=int(input("请输入“音乐剧云次方净化站”所在分组组号num："))
if user.find('@')>=0:
    print("请注意网页验证提示") 

#此处改为chromedriver的本地位置(windows系统注意去掉后面的.exe)
driver = webdriver.Chrome(executable_path="***************")

#全屏（如需要全屏，将下一行取消注释即可）
#driver.maximize_window()

driver.get(weiboUrl)
st=time.time()
time.sleep(3)
driver.find_element_by_id('loginName').clear()
driver.find_element_by_id('loginName').send_keys(user)
driver.find_element_by_id('loginPassword').clear()
driver.find_element_by_id('loginPassword').send_keys(password)
driver.find_element_by_id('loginAction').click()

#若邮箱登录，需要经过人工验证
if user.find('@')>=0:
    print("【请在网页进行手动验证】")

st=time.time()
while(time.time()-st<30):
    focus=driver.find_elements_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/ul/li[1]/span[1]')
    if len(focus)!=0:
        break
else:
    print("---Website Error--")
focus[0].click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div/div[1]/div[2]/ul/li['+str(num)+']/span').click() #特别关注
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div[1]/header/div[2]/div/a/h3').click()
k=int(input("请输入第__条卡黑帖：")) 
print("【用户输入完毕】")
btn = driver.find_element_by_xpath('//*[@id="app"]/div/'+'div['+str(k+1)+']/div/div/footer/div[2]')#查找评论按钮
btn.click()
st=time.time()

time.sleep(1)
test=driver.find_elements_by_class_name("m-img-box")
verify=test[0].get_attribute('href')
l=len(verify)
if verify[(l-10):l]!="5521179668" and verify[(l-10):l]!="7413113212":
    print("---Identity Error---")
    driver.close()
    sys.exit()
time.sleep(3)
links=driver.find_elements_by_link_text("网页链接")
length=len(links)
print("待处理数量：",length)
curUrl=driver.current_url
for i in range(0,length):
    
    st=time.time()
    while(time.time()-st<30):
        links=driver.find_elements_by_link_text("网页链接")
        if len(links)==length:
            break
    else:
        print("---Link Error---")
        driver.close()
        sys.exit()
    #print(len(links))
    
    target=links[i]
    driver.execute_script("arguments[0].scrollIntoView();", target)
    driver.execute_script('window.scrollBy(0,-100)')
    links[i].click()
    st=time.time()
    while(time.time()-st<10):
        tab1=driver.find_elements_by_link_text("有害信息")
        if len(tab1)!=0:
            break

    if len(tab1) == 0 :
        time.sleep(0.5)
        driver.get(curUrl)
        continue
    tab1[0].click()
    driver.execute_script('window.scrollBy(0,100)')
    tab2=driver.find_element_by_link_text("其他有害信息")
    tab2.click()
    driver.execute_script('window.scrollBy(0,200)')
    time.sleep(0.5)
    #点击选框
    check = driver.find_elements_by_class_name('inp_chk')
    check[len(check)-1].click()
    time.sleep(0.2)
    submit=driver.find_element_by_link_text("提交")
    submit.click()
    time.sleep(0.5)
    driver.get(curUrl)
    print('\r'+str(int(((i+1)*100)/length))+'%', end='')

print('\nDONE')