# Gauntlet 卡黑
 <img width="499" height="332" src="https://github.com/AllForClouds/Gauntlet/blob/master/Gauntlet.jpg"/>
 
*莫嚣张，有位骑士已刺出长枪*  
*And a knight with his banners all bravely unfurled*  
*惩恶扬善游侠四方*  
*Now hurls down his gauntlet to thee*  

## 功能说明  

* 1.0:（2020.6.26.)  
>1. 查找“音乐剧云次方净化站”第一条卡黑帖，评论打卡  
>2. 识别“音乐剧云次方净化站”卡黑格式，仅用于卡黑举报  
>3. 完成举报操作之后楼中楼打卡  

## 环境配置

* Python3
* Mac电脑Chrome浏览器
* selenium  
    ```
        pip install selenium
    ```

## 运行说明
【或许还有bug还有bug】
1. 配置好需要的环境
2. 下载好Chrome浏览器对应的webdriver(即chromedriver.exe)
3. 将“音乐剧云次方净化站”单独放入一个关注收藏分组，记录其序号num（如在默认中“特别关注”分组序号为6）
4. 在gauntlet.py中改动username和password
5. 在gauntlet.py中改动chromedriver.exe的本地位置
6. 在gauntlet.py中注释标出的地方改动序号为num
7. 在终端输入python3 gauntlet.py运行即可

## 待补充功能
1. 由于网速以及渣浪bug，有时分组页面没能成功加载（秃头程序员惨痛经历：测试中无数次点进蒸煮wb…差点在评论留下迷惑打卡bug……） 因此暂时关掉自动评论功能，请麻烦手动打卡orz…… 
2. 交互极其复杂，亟需改进
3. 功能单一，目前仅能进行网页链接举报