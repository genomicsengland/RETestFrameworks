import pytest

@pytest.mark.smoke
def testAddItems():
    print("Added items")
@pytest.mark.regression
def testCalculation():
    assert 2 + 2 == 4