# Gauntlet卡黑程序配图版说明
1. 配置好需要的环境(以下4项必须！)
   - Python3: 零基础安装推荐搜索Thonny，直接安装；该IDE特别特别友好！！！其他什么都不用装:)  
     - [官网链接](https://thonny.org)
     - 点击右上角与电脑系统对应的链接下载安装
      <div align=center><img width="550" height="580" src="https://github.com/AllForClouds/Gauntlet/blob/master/dir/thonny.jpg"/></div>  
   - 运行程序的开发环境(IDE): 依据个人喜好即可，有Thonny则不用安装其他
   - Chrome浏览器：直接搜索安装，无特别说明  
   - selenium:  
      - Thonny使用者：上边栏tools->manage packages->搜索selenium->点击安装（特别方便巨好用）  
         - 点击上边栏tools->manage packages  
            <div align=center><img width="630" height="180" src="https://github.com/AllForClouds/Gauntlet/blob/master/dir/tool.png"/></div>     
         - 输入selenium，点击右侧按钮搜索，搜索后点击下方install按钮，安装结束后关闭  
            <div align=center><img width="630" height="420" src="https://github.com/AllForClouds/Gauntlet/blob/master/dir/selenium.png"/></div>  
      - 其他IDE：终端输入pip install selenium
         - Mac:打开Mac系统中自带Terminal(终端)软件，输入pip install selenium
         - Windows:(不太熟悉windows命令行，如使用不熟练或安装不成功，推荐下载Thonny软件)  
2. 下载好Chrome浏览器对应的webdriver: [官方下载链接](https://sites.google.com/a/chromium.org/chromedriver/home) 需要翻墙，注意下载对应版本；如翻墙或下载有困难，百度搜索“Chrome webdriver”有很多下载指导
  - 首先获知Chrome浏览器版本，在地址框中输入
    ```
    chrome://version
    ```
    然后回车，可以看到chrome浏览器版本  
    如图中83.0.4103.116  
    <div align=center><img width="810" height="180" src="https://github.com/AllForClouds/Gauntlet/blob/master/dir/chrome.png"/></div>
  - 打开官方下载链接，找到对应版本号的链接(如图中下划线部分)，点击，选择mac或win系统对应的安装包下载安装  
    <div align=center><img width="810" height="810" src="https://github.com/AllForClouds/Gauntlet/blob/master/dir/webdriver.png"/></div>  
    下载并解压得到chromedriver，记得存chromedriver的位置  
3. 将“音乐剧云次方净化站”单独放入一个微博关注收藏分组，记录其序号num:  
   电脑端进入[网页](https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F) 登陆，点击“关注“旁边的小三角，可以数出所在分组从左至右从上至下的序号，如图中“特别关注”分组序号为6
   <div align=center><img width="500" height="200" src="https://github.com/AllForClouds/Gauntlet/blob/master/dir/focus.png"/></div> 
4. 在github上一页面中点击绿色的clone，下载本程序，并解压
   <div align=center><img width="810" height="270" src="https://github.com/AllForClouds/Gauntlet/blob/master/dir/download.png"/></div> 
5. 以下为具体运行程序步骤:   
   1. 打开 gauntlet.py  
    - Thonny使用者:  
      上边栏中File->Open, 选择并打开下载解压后的 gauntlet.py  
       <div align=center><img width="540" height="180" src="https://github.com/AllForClouds/Gauntlet/blob/master/dir/open.png"/></div>  
    - 其他IDE:(其他对应打开方式)  
   2. 在gauntlet.py中改动chromedriver的本地位置(见代码中第一个#注释标出部分)  
    - 找到chromdriver的本地位置:  
      Mac:打开自带的Terminal(终端)，将chromedriver拖动到显示框里，可以看到 \$ 后显示路径，即为本地位置，复制 \$ 后这一串  
      Windows:打开终端（同时按下键盘上win+r，输入cmd回车），将chromedriver拖动到显示框里，可以看到>>后显示路径，即为本地位置，复制>>后这一串  
    - 找到代码中改动位置，替换掉#注释下一行中引号部分  
      <div align=center><img width="810" height="210" src="https://github.com/AllForClouds/Gauntlet/blob/master/dir/code.png"/></div>   
   3. 运行gauntlet.py  
    - Thonny使用者:点击上方绿底白色小三角  
       <div align=center><img width="540" height="540" src="https://github.com/AllForClouds/Gauntlet/blob/master/dir/run.png"/></div>   
    - 其他IDE:(其他对应运行方式)  
   4. 运行时依照提示输入微博账号、密码  
      \[如果是邮箱登录，可能需要人工验证，已设置等待时间10s，请手动验证\]  
   5. 运行时依照提示输入分组组号num  
   6. 运行时依照提示输入第k条帖（即从上到下第几条是带链接卡黑帖）  
  
