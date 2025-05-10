from src.math_operation import add,sub 

def test_add():
    assert add(3,6)==9
    assert add(-8,-8)==-16
    assert add(0,0)==0
    assert add(6,5)==11

def test_sub():
    assert sub(3,6)==-3
    assert sub(-8,-6)==-2


