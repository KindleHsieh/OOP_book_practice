# -*- coding: utf-8 -*-
# author: Kindle Hsieh time: 2021/10/28
from __future__ import annotations
from typing import Any, Callable

#
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

def setup_module(module: Any) -> None:
    print(f"setting up MODULE {module.__name__}")


def teardown_module(module: Any) -> None:
    print(f"tearing down MODULE {module.__name__}")


def test_a_function() -> None:
    print("RUMMING TEST FUMCTION")


class BaseTest:
    @classmethod
    def setup_class(cls: type["BaseTest"]) -> None:
        print(f"setting up CLASS {cls.__name__}")

    @classmethod
    def teardown_class(cls: type['BaseTest']) -> None:
        print(f"tearing down CLASS {cls.__name__}")

    def setup_method(self, method: Callable[[], None]) -> None:
        print(f"setting up METHOD {method.__name__}")

    def teardown_method(self, method: Callable[[], None]) -> None:
        print(f"tearing down METHOD {method.__name__}")


class TestClass1(BaseTest):
    def test_method_1(self) -> None:
        print("Running METHOD 1-1")

    def test_method_2(self) -> None:
        print("Running METHOD 1-2")


class TestClass2(BaseTest):
    def test_method_1(self) -> None:
        print("Running METHOD 2-1")

    def test_method_2(self) -> None:
        print("Running METHOD 2-2")
