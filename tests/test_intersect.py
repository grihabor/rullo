import pytest


@pytest.mark.parametrize('x,y,expected', [
    ([(1,), (2,)], 
     [(1,3,2), (2,3,3), (3,1,2), (1,1,1), (3,2)],
     [(1,3,2), (2,3,3), (1,1,1)],),
])
def test_intersect(x, y, expected):
    from rullo.intersection import _intersect

    assert expected == _intersect(x, y)
    
    