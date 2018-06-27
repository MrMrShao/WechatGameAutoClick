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


def read_question(f):
    time.sleep(1)
    response = json.load(f)
    f.close()
    os.remove('D:\ADB\question\jjds.iwillgo.cn\index\index_one_nine_six\sprint_game')
    for i in range(40):
        is_true = response[str(i)]['is_true']
        #time.sleep(0.5)
        adb_tap('option' + str(is_true))
        print(i)
    return response


class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        print('go')
        global answer
        if event.src_path.split('\\')[-1] == 'sprint_game':
            with open('D:\ADB\question\jjds.iwillgo.cn\index\index_one_nine_six\sprint_game', encoding='utf-8') as f:
                answer = read_question(f)
            print(f)


if __name__ == "__main__":
    os.remove('D:\ADB\question\jjds.iwillgo.cn\index\index_one_nine_six\sprint_game')
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, r"D:\ADB\question\jjds.iwillgo.cn\index\index_one_nine_six\\", True)
    print('助手已经运行，请开始游戏')
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrup:
        observer.stop()
    observer.join()
