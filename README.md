# Gauntlet 卡黑
<div align=center><img width="499" height="332" src="https://github.com/AllForClouds/Gauntlet/blob/master/Gauntlet.jpg"/></div>
 
*莫嚣张，有位骑士已刺出长枪*  
*And a knight with his banners all bravely unfurled*  
*惩恶扬善游侠四方*  
*Now hurls down his gauntlet to thee*  

## 功能说明  

* 1.0:（2020.6.26.)  
>1. 查找“音乐剧云次方净化站”第k条卡黑帖 
>2. 识别“音乐剧云次方净化站”卡黑格式，点开第k条中所有链接进行卡黑举报（目前所有举报仅提供"有害-其他"）

## 环境配置

* Python3
* Mac电脑Chrome浏览器
* selenium  
    ```
        pip install selenium
    ```

## 操作步骤
1. 配置好需要的环境
2. 下载好Chrome浏览器对应的webdriver(即chromedriver.exe)（[官方下载链接](https://sites.google.com/a/chromium.org/chromedriver/home) 需要翻墙，注意下载对应版本；如翻墙有困难，百度搜索“Chrome webdriver”有很多下载指导）
3. 将“音乐剧云次方净化站”单独放入一个关注收藏分组，记录其序号num（即点击“关注“旁边的小三角，可以数出所在分组从左至右从上至下的序号，如在默认中“特别关注”分组序号为6）
4. 在gauntlet.py中改动chromedriver.exe的本地位置
5. 在终端输入python3 gauntlet.py运行
6. 运行时依照提示输入账号、密码
7. 【如果是邮箱登录，可能需要人工验证，已设置等待时间10s，请手动验证】
8. 运行时依照提示输入分组组号num
9. 运行时依照提示输入第k条卡黑帖
10. 运行过程中会显示待处理数量以及进度条，卡黑完成后会输出“DONE”，退出程序
    
输入示例：
```
python3 gauntlet.py
xxxxxxxxxxx(电话号码)
xxxxxxxx（密码）
6（特别关注组组号）
1（第1条卡黑帖）
```
输出示例：
```
待处理数量：
4
100%
DONE
```
## 补充说明
1. 由于渣浪服务器和网速原因，偶尔出现页面跳转中途退出程序出错情况，为加载过慢所致，一般再次尝试即可解决
2. 目前程序运行速度不甚理想，与1中原因一致，是为保证网页完全加载
3. 本机测试Chrome浏览器可保证顺利运行，如果相同配置下出现bug，大概率与网速和显示屏大小有关  
    网速解决方案：等网络条件较好时再次尝试；  
    显示屏大小解决方案：调节代码注释中“向下滚动”的具体数值/在注释中标出部分将”全屏“那一行取消注释


## 待补充功能
1. 由于网速以及渣浪bug，有时分组页面没能成功加载（秃头程序员惨痛经历：测试中无数次点进蒸煮wb…差点在评论留下迷惑打卡bug……） 因此暂时关掉自动评论功能，请麻烦手动打卡orz…… 
2. 交互极其复杂，亟需改进
3. 功能单一，目前仅能进行网页链接举报
4. 待添加云女/滇身份识别功能
5. 其他浏览器/系统开发（gauntlet_safari.py目前不能使用）

