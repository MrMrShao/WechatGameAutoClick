# _*_ coding:utf-8 _*_
from watchdog.observers import Observer
from watchdog.events import *
import time
import json
import os

# option0是错号的坐标，option1是对号的坐标
conf = {
    "option0": {
        "x": 810,
        "y": 1650,
    },
    "option1": {
        "x": 270,
        "y": 1650,
    }
}


# 点击相应坐标
def adb_tap(option):
    os.system('adb shell input tap {0} {1}'.format(conf[option]['x'], conf[option]['y']))


# 顺次点击40道题的答案
def read_question(response):
    global start
    global num
    # 每次抓包可以得到40个答案
    for i in range(40):
        # 游戏开始有个开场动画，需要等待一下再点击
        if start:
            start = False
            time.sleep(2)
        is_true = response[str(i)]['is_true']
        adb_tap('option' + str(is_true))
        if i != 39:
            time.sleep(sleep_time)
        num += 1
        print("第{}道题, {}".format(num, is_true))


# 监控json文件变化
class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        if os.path.exists(path):
            with open(path) as f:
                # 获得json，解析，删除json
                time.sleep(sleep_time)
                response = json.load(f)
                f.close()
                os.remove(path)
                read_question(response)


if __name__ == "__main__":
    # 更改！保存的json文件
    path = 'D:\ADB\question\jjds.iwillgo.cn\index\index_one_nine_six\sprint_game'
    sleep_time = 0.05
    start = True
    # 答题数目
    num = 0
    # 判断一下是否有之前残存的json，有就先删除
    if os.path.exists(path):
        os.remove(path)
    """
    watchdog主要采用观察者模型。主要有三个角色：observer，event_handler，被监控的文件夹。
    三者原本是独立的，主要通过observer.schedule函数将三者串起来，
    observer不断检测调用平台依赖代码对监控文件夹进行变动检测.当发现改变时，通知event_handler处理。
    """
    observer = Observer()
    event_handler = FileEventHandler()
    # 更改！保存的json文件所属位置
    observer.schedule(event_handler, r'D:\ADB\question\jjds.iwillgo.cn\index\index_one_nine_six\\', True)
    print('助手已经运行，请开始游戏')
    observer.start()
    try:
        while True:
            time.sleep(0)
    except KeyboardInterrup:
        observer.stop()
    observer.join()
