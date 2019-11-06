# This is the first python code 
from mathlib import cal_addition, cal_product

from pytest import mark, param
testdata1 = [param(2 , 2,4, id="positive"), param(2,0, 2, id="zero"), param(-1,4, 3, id="negative")]
testdata2 = [param(2 , 2,4, id="positive"), param(2,0, 0, id="zero"), param(-1,4, -4, id="negative")]
@mark.parametrize("a, b, expected", testdata1)
def test_cal_add(a,b, expected):
    som = cal_addition(a, b)
    assert som == expected
@mark.parametrize("c, d, expected", testdata2)
def test_cal_multi(c, d, expected):
    pro = cal_product(c, d)
    assert pro == expected
    
