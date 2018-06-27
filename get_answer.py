# _*_ coding:utf-8 _*_
from watchdog.observers import Observer
from watchdog.events import *
import time
import json
import os

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


def adb_tap(option):
    os.system('adb shell input tap {0} {1}'.format(conf[option]['x'], conf[option]['y']))


def read_question(response):
    global sleep_time
    global start
    sleep_time = response[str(0)]['seconds'] / 8
    for i in range(40):
        if start:
            start = False
            time.sleep(2)
        is_true = response[str(i)]['is_true']
        adb_tap('option' + str(is_true))
        if i != 39:
            time.sleep(sleep_time)
        print(i)


class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        global sleep_time
        if os.path.exists(path):
            with open(path) as f:
                time.sleep(sleep_time)
                print(sleep_time)
                response = json.load(f)
                f.close()
                os.remove(path)
                read_question(response)


if __name__ == "__main__":
    path = 'D:\ADB\question\jjds.iwillgo.cn\index\index_one_nine_six\sprint_game'
    sleep_time = 5 / 8
    start = True
    if os.path.exists(path):
        os.remove(path)
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, r'D:\ADB\question\jjds.iwillgo.cn\index\index_one_nine_six\\', True)
    print('助手已经运行，请开始游戏')
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrup:
        observer.stop()
    observer.join()
