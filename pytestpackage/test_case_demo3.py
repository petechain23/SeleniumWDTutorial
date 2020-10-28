import pytest


@pytest.fixture()
def setUp():
    print("\nSetup every method demo3")
    yield
    print("\nTearDown every method demo3")


def test_methodA(setUp):
    print("\nRuning method demo3 A")


def test_methodB(setUp):
    print("\nRuning method demo3 B")
