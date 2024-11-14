import os
from typing import Any

import pytest

from src.decorators import log


@pytest.fixture
def create_file_ok() -> str:
    if os.path.basename(os.getcwd()) == "HomeWork_9.1":
        filename = "logs/test_log_ok_file.txt"
    else:
        filename = "../logs/test_log_ok_file.txt"
    file = open(filename, "w", encoding="utf-8")
    file.close()
    return filename


@pytest.fixture
def create_file_err() -> str:
    if os.path.basename(os.getcwd()) == "HomeWork_9.1":
        filename = "logs/test_log_division_by_zer_file.txt"
    else:
        filename = "../logs/test_log_division_by_zer_file.txt"
    file = open(filename, "w", encoding="utf-8")
    file.close()
    return filename


def test_log_ok_console(capsys: Any) -> None:
    @log()
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out.split("\n")[1] == " my_function ok"


def test_log_division_by_zer_console(capsys: Any) -> None:
    @log()
    def my_division(x: int, y: int) -> float:
        return x / y

    my_division(5, 0)
    captured = capsys.readouterr()
    assert captured.out.split("\n")[1] == " my_division error: division by zero. Inputs: (5, 0), {}"


def test_log_ok_file(create_file_ok: str) -> None:
    @log(create_file_ok)
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, 2)
    with open(create_file_ok, "r", encoding="utf-8") as file:
        log_data = file.read()
    assert log_data.split("\n")[-4] == "my_function ok"


def test_log_division_by_zer_file(create_file_err: str) -> None:
    @log(create_file_err)
    def my_division(x: int, y:int) -> float:
        return x / y

    my_division(5, 0)
    with open(create_file_err, "r", encoding="utf-8") as file:
        log_data = file.read()
    assert log_data.split("\n")[-4] == "my_division error: division by zero. Inputs: (5, 0), {}"
