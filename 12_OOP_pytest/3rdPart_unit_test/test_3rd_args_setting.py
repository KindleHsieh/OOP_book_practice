# -*- coding: utf-8 -*-
# author: Kindle Hsieh time: 2021/10/31

# 目前為止都沒有設置參數，如同unitest飯粒的StatsList.
# pytest 有兩種設置方式：
# 第一種是利用
# @pytest.fixture
# def var_name():
#     return value
# 此種方式是在單一module上使用(通用)。

# 第二種是建立conftest.py，這種就類似『全域』，可以再多module內傳送。。
from __future__ import annotations
from stats import StatsList
import pytest


@pytest.fixture
def valid_stats() -> StatsList:
    return StatsList([1, 2, 2, 3, 3, 4])


def test_mean(valid_stats: StatsList) -> None:
    assert valid_stats.mean() == 2.5


def test_median(valid_stats: StatsList) -> None:
    assert valid_stats.median() == 2.5
    valid_stats.append(4)
    assert valid_stats.median() == 3


def test_mode(valid_stats) -> None:
    assert valid_stats.mode() == [2, 3]
    valid_stats.remove(2)
    assert valid_stats.mode() == [3]


# If implement @pytest.fixture as a generator, it can also run like teardown.
import tarfile
from pathlib import Path
import hashlib
import pytest
from typing import Iterator
import sys

def checksum(source: Path, checksum_path: Path) -> None:
    if checksum_path.exists():
        backup = checksum_path.with_stem(f"(old) {checksum_path.stem}")
        backup.write_text(
            checksum_path.read_text()
        )
    checksum = hashlib.sha256(source.read_bytes())
    checksum_path.write_text(f"{source.name}, {checksum.hexdigest()}")

@pytest.fixture
def working_directory(tmp_path: Path) -> Iterator[tuple[Path, Path]]:
    working = tmp_path / "some_directory"
    working.mkdir()
    source = working / "data.txt"
    source.write_bytes(b"Hello, world!\n")
    checksum = working / "checksum.txt"
    checksum.write_text("data.txt Old_Checksum")
    yield source, checksum

    checksum.unlink()
    source.unlink()