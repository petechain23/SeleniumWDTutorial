import pytest


@pytest.fixture()
def setUp():
    print("Once before every method demo1")


def test_methodA(setUp):
    print("Runing method demo1 A")


def test_methodB(setUp):
    print("Runing method demo1 B")
