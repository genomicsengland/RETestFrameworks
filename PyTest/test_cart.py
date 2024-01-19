import pytest

@pytest.fixture(scope="session",autouse=True)
def setUp():
    print("Launch Browser")
    print("Login")
    print("Browse Products")

    yield
    print("LogOff")
    print("Close Browser")

def testAddItemtoCart(setUp):
    print("Add Item Successful")
def testRemoveItemFromCart(setUp):
    print("Remove Item Successful")
