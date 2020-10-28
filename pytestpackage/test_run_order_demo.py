import pytest


@pytest.mark.run(order=2)
def test_methodA(oneTimeSetUp, setUp):
    print("\nRuning method A config test order")


@pytest.mark.run(order=3)
def test_methodB(oneTimeSetUp, setUp):
    print("\nRuning method B config test order")


@pytest.mark.run(order=1)
def test_methodC(oneTimeSetUp, setUp):
    print("\nRuning method C config test order")


@pytest.mark.run(order=6)
def test_methodD(oneTimeSetUp, setUp):
    print("\nRuning method D config test order")


@pytest.mark.run(order=5)
def test_methodE(oneTimeSetUp, setUp):
    print("\nRuning method E config test order")


@pytest.mark.run(order=4)
def test_methodF(oneTimeSetUp, setUp):
    print("\nRuning method F config test order")
