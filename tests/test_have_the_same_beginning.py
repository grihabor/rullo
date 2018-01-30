
@pytest.mark.parametrize('pair,expected', [
    ([(1,), (1,3,3,)], True),
    ([(2,3,1,), (3,)], False),
    ([(2,3,), (2,1,)], False),
])
def test_have_the_same_beginning(pair, expected):
    from rullo.intersection import _have_the_same_beginning

    assert expected == _have_the_same_beginning(*pair)
