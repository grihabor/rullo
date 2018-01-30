import pytest


@pytest.mark.parametrize('outcomes,expected', [
    ((
        [(1,), (2,)],
        [(1,3,2), (2,3,3), (3,1,2), (1,1,1), (3,2)],
    ), [(1,3,2), (2,3,3), (1,1,1)],),
])
def test_outcome_intersection(outcomes, expected):
    from rullo.intersection import _outcome_intersection

    assert set(expected) == set(_outcome_intersection(*outcomes))


