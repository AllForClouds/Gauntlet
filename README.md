# Gauntlet 卡黑
<div align=center><img width="499" height="332" src="https://github.com/AllForClouds/Gauntlet/blob/master/Gauntlet.jpg"/></div>
 
*莫嚣张，有位骑士已刺出长枪*  
*And a knight with his banners all bravely unfurled*  
*惩恶扬善游侠四方*  
*Now hurls down his gauntlet to thee*  
*——《我，堂吉诃德》*

## 功能说明  

* 1.0:（2020.6.26.\[2020.7.8.更新\])  
>1. 查找“音乐剧云次方净化站”第k条卡黑帖 
>2. 识别“音乐剧云次方净化站”卡黑格式，点开第k条中所有链接进行卡黑举报（目前所有举报仅提供"有害-其他"）

## 环境配置
* Python3
* Chrome浏览器(Mac, Windows均可使用)
* selenium  

## 操作步骤
[详细配图版说明](https://github.com/AllForClouds/Gauntlet/blob/master/direction.md)
1. 配置好需要的环境  
   - Python3:零基础安装推荐搜索thonny，直接安装；该IDE特别特别友好！！！其他什么都不用装:)  
   - Chrome浏览器：直接搜索安装，无特别说明  
   - selenium：
     - Thonny使用者：上边栏tools->manage packages->搜索selenium->点击安装（特别方便巨好用）；
     - 其他IDE：终端输入pip install selenium
2. 下载好Chrome浏览器对应的webdriver（[官方下载链接](https://sites.google.com/a/chromium.org/chromedriver/home) 需要翻墙，注意下载对应版本；如翻墙/下载有困难，百度搜索“Chrome webdriver”有很多下载指导）
3. 将“音乐剧云次方净化站”单独放入一个微博关注收藏分组，记录其序号num（即点击“关注“旁边的小三角，可以数出所在分组从左至右从上至下的序号，如在默认中“特别关注”分组序号为6）
4. 在gauntlet.py中改动chromedriver.exe的本地位置（见#注释标出部分）
5. 运行gauntlet.py
6. 运行时依照提示输入账号、密码
   【如果是邮箱登录，可能需要人工验证，已设置等待时间10s，请手动验证】
7. 运行时依照提示输入分组组号num
8. 运行时依照提示输入第k条帖
9. 运行过程中会显示待处理数量以及进度条，卡黑完成后会输出“DONE”，退出程序
    
输入示例：
```
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
1. 目前该程序识别“音乐剧云次方净化站”，仅能处理“有害-其他”，如果有其他举报（一般情况较少）烦请手动操作；打卡也仍需要手动(orz会尽快解决的)
2. 可自动运行，但不可将浏览器最小化
3. 由于渣浪服务器和网速原因，偶尔出现页面跳转中途退出程序出错情况，为加载过慢所致，一般再次尝试即可解决
4. 目前程序运行速度不甚理想，与3中原因一致，是为保证网页完全加载
5. 本机测试Chrome浏览器可保证顺利运行，如果相同配置下出现bug，大概率与网速有关，麻烦等网络条件较好时再次尝试。  

## 待补充功能
1. 由于网速以及渣浪bug，有时分组页面没能成功加载（秃头程序员惨痛经历：测试中无数次点进蒸煮wb…差点在评论留下迷惑打卡bug……） 因此暂时关掉自动评论功能，请麻烦手动打卡orz…… 
2. 交互极其复杂，亟需改进
3. 功能单一，目前仅能进行网页链接举报
4. 待添加云女/滇身份识别功能
5. 其他浏览器/系统开发

