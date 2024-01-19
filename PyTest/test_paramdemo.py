import pytest

@pytest.mark.parametrize("a,b,final",[(2,6,8),(1,2,7)])
def testAdd(a,b,final):
    assert a+b == final