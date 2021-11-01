# -*- coding: utf-8 -*-
# author: Kindle Hsieh time: 2021/10/31

import py.test

@py.test.mark.skipif('sys.version_info <= (3, 0)')
def test_python3():
    assert b'hello'.decode() == 'hello'
