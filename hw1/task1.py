import pytest

#function printing hello world
def f():
    print("Hello, World!")

#function takes output, analyses it and determines correctness using pytest
def test_func(capsys):
    f()
    var1 = capsys.readouterr()
    assert var1.out == "Hello, World!\n"