# WechatGameAutoClick
微信小游戏《加减大师》辅助工具，抓包+模拟点击

##游戏介绍
《加减大师》是一款微信小游戏，玩家在指定时间内判断等式的对错，答对越多得分越多，每周得分的前500名可以兑换娃娃等礼品。<br>
<div align=center>
<img width="150" height="250" src="https://github.com/tiantianwahaha/WechatGameAutoClick/raw/master/img/example1.png"/>
<img width="150" height="250" src="https://github.com/tiantianwahaha/WechatGameAutoClick/raw/master/img/example2.png"/>
<img width="150" height="250" src="https://github.com/tiantianwahaha/WechatGameAutoClick/raw/master/img/example3.png"/>
</div>

**WechatGameAutoClick**是用python3实现的一个简单脚本。<br>
不同于其他的截图识别题目然后模拟点击的脚本，本程序通过Charles软件抓包获得题目和答案，通过ADB模拟点击，60行代码就基本搞定。

##效果展示

##使用方法

* 下载代码到本地
```

```
* 安装所需要的包
```
用于监控抓包获得的数据的变化情况
pip install watchdog
```

* 安装配置Charles
* 配置ADB
* 运行程序
```
python get_answer.py
注意，我的手机为小米6，屏幕尺寸为1920*1080，所以我的手机对号和错号的中心位置坐标分别为(270,1650),(810,1650)
如果屏幕尺寸不一致，请修改为合适的大小。
```

##参考
知乎答题王（头脑王者）全自动答题辅助[wechat_brain](https://github.com/251321639/wechat_brain)
