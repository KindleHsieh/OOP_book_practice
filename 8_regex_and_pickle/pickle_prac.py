# -*- coding: utf-8 -*-
# author: Kindle Hsieh time: 2021/10/23

# Custom pickle.
# 自訂pickle只要是因為有些情形，pickle是無法處理的(序列化)。
# 無法序列化的原因有： 時間敏感度、之後載入就不合理的屬性。
# 例如 開啟中的網路socket、檔案、執行中的執行緒或資料連線儲存在物件的屬性中。 有的情況就會直接報error.
# 下面以threading.Timer為例。

from threading import Timer
import datetime
from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


class UpdatedURL:
    def __init__(self, url):
        self.url = url
        self.contents = ''
        self.last_updated = None
        self.update()

    def update(self):
        self.contents = urlopen(self.url).read()
        self.last_updated = datetime.datetime.now()
        self.schedule()

    def schedule(self):
        self.timer = Timer(3600, self.update)
        self.timer.setDaemon(True)
        self.timer.start()


class UpdatedURL_Custom_wo_Timer:
    def __init__(self, url):
        self.url = url
        self.contents = ''
        self.last_updated = None
        self.update()

    def update(self):
        self.contents = urlopen(self.url).read()
        self.last_updated = datetime.datetime.now()
        self.schedule()

    def schedule(self):
        self.timer = Timer(3600, self.update)
        self.timer.setDaemon(True)
        self.timer.start()

    def __getstate__(self):
        """
        自訂pickle時，如果沒有此屬性，他就會選擇直接儲存物件的__dict__屬性。
        不然此屬性會優先處理。

        但在這方法結束時有return，是因為此物件只要用來儲存能存的，沒有要復歸。
        需使用某種方式復原物件的屬性。
        """

        new_state = self.__dict__.copy()
        if 'timer' in new_state:
            del new_state['timer']
        return new_state


class UpdatedURL_Custom_w_Timer:
    def __init__(self, url):
        self.url = url
        self.contents = ''
        self.last_updated = None
        self.update()

    def update(self):
        self.contents = urlopen(self.url).read()
        self.last_updated = datetime.datetime.now()
        self.schedule()

    def schedule(self):
        self.timer = Timer(3600, self.update)
        self.timer.setDaemon(True)
        self.timer.start()

    def __getstate__(self, state):
        """
        接續上面，此方法不需要return 因為我們還要設定__getstate__。
        """

        new_state = self.__dict__.copy()
        if 'timer' in new_state:
            del new_state['timer']

    def __setstate__(self, state):
        self.__dict__ = state
        self.schedule()



if __name__ == '__main__':
    import pickle

    try:
        u = UpdatedURL('https://www.google.com/?client=safari')
        serialized = pickle.dumps(u)
        """ TypeError: can't pickle _thread.lock objects """
    except TypeError as e:
        print("Error: ", e)

    u_wo_timer = UpdatedURL_Custom_wo_Timer('https://www.google.com/?client=safari')
    print(u_wo_timer.timer)

    u_w_timer = UpdatedURL_Custom_w_Timer('https://www.google.com/?client=safari')
    print(u_w_timer.timer)