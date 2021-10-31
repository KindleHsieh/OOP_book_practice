# -*- coding: utf-8 -*-
# author: Kindle Hsieh time: 2021/10/28

def test_int_float():
    assert 1 == 1.0


class TestNumbers:
    def test_int_float(self):
        assert 1 == 1.0

    def test_int_srt(self):
        assert 1 == '1'


# class 中的 setup_method -> unittest setUp.
# class 中的 teardown_method -> unittest tearDown.
# 但是 pytest提供各種層級(module, class, method)的 setup 與 teardown.

def setup_module(module):
    print(f"setting up MODULE {module.__name__}")


def teardown(module):
    print(f"tearing down MODULE {module.__name__}")


def test_a_function():
    print("RUMMING TEST FUMCTION")


class BaseTest:
    def setup_class(cls):
        print(f"setting up CLASS {cls.__name__}")

    def teardown_class(cls):
        print(f"tearing down CLASS {cls.__name__}")

    def setup_method(self, method):
        print(f"setting up METHOD {method.__name__}")

    def teardown_method(self, method):
        print(f"tearing down METHOD {method.__name__}")


class TestClass1(BaseTest):
    def test_method_1(self):
        print("Running METHOD 1-1")

    def test_method_2(self):
        print("Running METHOD 1-2")


class TestClass2(BaseTest):
    def test_method_1(self):
        print("Running METHOD 2-1")

    def test_method_2(self):
        print("Running METHOD 2-2")

# 因為當測試成功，就不會執行print的函式，這是pytest的預設，因此不會有函式內的print內容。
# 如果要有的話，就要執行： py.test <module.py> -s
# ex py.test 12_OOP_pytest/3rdPart_unit_test/3rd_pytest_test.py -s

# # 目前為止都沒有設置參數，如同unitest飯粒的StatsList.
# # pytest 有兩種設置方式：
# # 第一種是利用func名稱。 def pytest_funcarg__<arg name>(request):
# # 此種方式是在單一module上使用(通用)。
# # request 提供方法與屬性來修改fumcarg的行為。
# # 第二種是建立conftest.py，這種就類似『全域』，可以再多module內傳送。。
# from .stats import StatsList
#
#
# def pytest_funcarg__valid_stats(request):
#     return StatsList([1, 2, 2, 3, 3, 4])
#
#
# def test_mean(valid_stats):
#     assert valid_stats == 2.5
#
#
# def test_median(valid_stats):
#     assert valid_stats.median() == 2.5
#     valid_stats.append(4)
#     assert valid_stats.median() == 3
#
#
# def test_mode(valid_stats):
#     assert valid_stats.mode() == [2, 3]
#     valid_stats.remove(2)
#     assert valid_stats.mode() == [3]
