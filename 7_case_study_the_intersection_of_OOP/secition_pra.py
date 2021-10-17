"""
reversed()
"""


# len + getitem.
# 會根據__len__的回傳數字，作為訪問__getitem__的次數，並遞減字訪問。
class CustomSequence:
    def __len__(self):
        return 5

    def __getitem__(self, item):
        return f"xP{item}"


# reversed.
# 會將__reversed__的字串，逐一回傳。
class FunkyBackWords():
    def __reversed__(self):
        return "BACKWARD!"


if __name__ == '__main__':
    normal_list = [1, 2, 3, 4, 5]

    for way in normal_list, CustomSequence(), FunkyBackWords():
        print(f'\n{way.__class__.__name__}: ', end='')
        for item in reversed(way):
            print(item, end=', ')
    print(f'\n{"-"*5} End. {"-"*5} ')


"""
With 的 背景執行實現。
"""


# 建構一個字串組合管理，先將資料存進list，最後離開時再合併起來。
class StringJoiner(list):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.result = " ".join(self)


class MyFile:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.name, mode=self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


# create background def by contextmanager
# notice! This func only can use once because it is a generator.
from contextlib import contextmanager


@contextmanager
def myfile(name, mode):
    file = open(name, mode)
    try:
        yield file

    except:
        file.close()


if __name__ == '__main__':
    import random, string

    with StringJoiner() as string_list:
        print(string.ascii_letters)
        for i in range(15):
            string_list.append(random.choice(string.ascii_letters))
    print(string_list.result)
    print(f'{"-" * 5} End. {"-" * 5} ')

"""
變數清單
"""


# kwargs.
class Options:
    default_options = {
        'port': 1,
        'host': 'local',
        'username': 'hihi',
        'pwd': 123,
    }

    def __init__(self, **kwargs):
        # 這邊使用到再創造一個dict不直接使用update self.default_options，因為update會直接將原來的option複寫掉。
        self.options = dict(self.default_options)
        self.options.update(kwargs)

    def __getitem__(self, item):
        return self.options[item]


if __name__ == '__main__':
    print(Options.default_options)
    oo = Options(**{'port': 8080, 'pwd': 456})
    print(oo.default_options)
    print(oo.options)
    pp = Options()
    print(pp.default_options)
    print(f'{"-" * 5} End. {"-" * 5} ')

"""
位置參數的練習應用。
"""
import shutil
import os.path
def augmented_move(tar_folder, *filenames, verbose=True, **specific):
    def print_verbose(message):
        if verbose:
            print(message)
            
    for filename in filenames:
        tar_path = os.path.join(tar_folder, filename)
        
        if filename in specific:
            if specific[filename] == 'ignore':
                print_verbose(f"Ignore {filename}")
            elif specific[filename] == 'copy':
                print_verbose(f"Copy {filename}")
                shutil.copyfile(filename, tar_path)
            else:
                print_verbose(f"No action about {filename}: {specific[filename]}")
        else:
            print_verbose(f"Moving {filename}")
            shutil.move(filename, tar_path)


"""

"""
import datetime
import time


class TimedEvent:
    def __init__(self, endtime, callback):
        self.callback = callback
        self.endtime = endtime

    def ready(self):
        return self.endtime <= datetime.datetime.now()


class Timmer:
    def __init__(self):
        self.events = []

    def call_after(self, delay: int, callback):
        """
        for adding event from now after time delay .
        """
        end_time = datetime.datetime.now() + datetime.timedelta(seconds=delay)
        self.events.append(TimedEvent(end_time, callback))

    def run(self):
        while True:
            ready_events = (e for e in self.events if e.ready())
            for event in ready_events:
                event.callback(self)
                self.events.remove(event)
            time.sleep(0.5)

if __name__ == '__main__':
    def format_time(message, *args):
        now = datetime.datetime.now().strftime("%I:%M:%S")
        print(f"P{now}: {message}")

    def one(timer):
        format_time("Called One.")

    def two(timer):
        format_time("Called Two.")

    def three(timer):
        format_time("Called Three.")

    class Repeater:
        def __init__(self):
            self.count = 0

        def repeater(self, timer):
            format_time(f"repeat {self.count}")
            self.count += 1
            timer.call_after(5, self.repeater)

    timer = Timmer()
    timer.call_after(1, one)
    timer.call_after(2, one)
    timer.call_after(2, two)
    timer.call_after(4, two)
    timer.call_after(3, three)
    timer.call_after(6, three)

    repeater = Repeater()
    timer.call_after(5, repeater.repeater)

    format_time("staring.....")
    timer.run()
