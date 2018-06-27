# WechatGameAutoClick
微信小游戏《加减大师》辅助工具，抓包+模拟点击

## 介绍
《加减大师》是一款微信小游戏，玩家在指定时间内判断等式的对错，答对越多得分越多，每周得分的前500名可以兑换娃娃等礼品。<br>
<div align=center>
<img width="150" height="250" src="https://github.com/tiantianwahaha/WechatGameAutoClick/raw/master/img/example1.png"/>
<img width="150" height="250" src="https://github.com/tiantianwahaha/WechatGameAutoClick/raw/master/img/example2.png"/>
<img width="150" height="250" src="https://github.com/tiantianwahaha/WechatGameAutoClick/raw/master/img/example3.png"/>
</div>

**WechatGameAutoClick**是用python3实现的一个简单脚本。<br>
不同于其他的截图识别题目然后模拟点击的脚本，本程序通过Charles软件抓包获得题目和答案，通过ADB模拟点击，60行代码就基本搞定。

## 效果展示

## 使用方法

1. 下载代码到本地
```
git clone https://github.com/tiantianwahaha/WechatGameAutoClick.git
```
2. 安装所需要的包
**用于监控抓包获得的数据的变化情况**
```
pip install watchdog
```

3. [安装配置Charles](https://github.com/tiantianwahaha/WechatGameAutoClick/wiki/Charles%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B)
4. [配置ADB]()
5. 运行程序
```
python get_answer.py
```
**注意，我的手机为小米6，屏幕尺寸为1920*1080，所以我的手机对号和错号的中心位置坐标分别为(270,1650),(810,1650)**<br>
**如果屏幕尺寸不一致，请修改为合适的大小。**
**记得把56行和63行改为你自己设置的抓包存储路径**


## 需要注意的问题
* 每次抓包可以得到40道题的答案，40道题答题时间减少依次(5,4,3,2,1,0.7)，最低为0.7。<br>
* 每次抓包json保存到本地以及解析需要时间，点击后等待切屏也需要时间，所以在这两个地方需要sleep(答题时间/8),网络不卡顺利抓包的情况下，理论上可以无限答题。

## 参考
知乎答题王（头脑王者）全自动答题辅助[wechat_brain](https://github.com/251321639/wechat_brain)
