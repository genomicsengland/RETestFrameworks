import pytest

@pytest.fixture(scope="session",autouse=True)
def tc_setup(browser):
    if browser == "chrome" :
        print("Launch Chrome browser")
        print("Login")
        print("Browse Products")
    else:
        print("Invalid Browser")
    yield
    print("Logoff")
    print("Close Browser")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session",autouse=True)
def browser(request):
    return request.config.getoption("--browser")