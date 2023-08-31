import os
from source.main import is_extension


def test_case_1():
    assert is_extension(".exe") is True


def test_case_2():
    assert is_extension(".png") is True


def test_case_3():
    assert is_extension(".png.") is False


def test_case_4():
    assert is_extension(".p.n.g") is False


def test_on_real_extensions():
    file_path = 'C:\\Users\\pavel\\PycharmProjects\\FindFileWithExtensions\\data\\extensions_list.txt'

    with open(file_path, 'r', encoding='utf-8') as file:
        extensions = file.readlines()

    for extension in extensions:
        assert is_extension(extension) is True
