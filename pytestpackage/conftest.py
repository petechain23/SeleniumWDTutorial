import pytest


@pytest.fixture()
def setUp():
    print("\nSetup before run every method")
    yield
    print("\nTearDown after run every method")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("\nSetup begin to run test case")
    if browser == 'firefox':
        value = 10
        print("Running tests on FF")
    else:
        value = 20
        print("Running tests on chrome")
    if request.cls is not None:
        request.cls.value = value

    yield value
    print("\nTearDown end when run all test case")


def pytest_addoption(parser):
    parser.addoption("--browser")
    # parser.addoption("--osType", help("Type of operating system"))
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
