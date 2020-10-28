import pytest


@pytest.fixture()
def setUp():
    print("\nOnce before every method demo2")
    yield
    print("\nOnce after every method demo2")


def test_methodA(setUp):
    print("\nRuning method demo2 A")


def test_methodB(setUp):
    print("\nRuning method demo2 B")
