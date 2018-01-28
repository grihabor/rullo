import pytest
import numpy as np


@pytest.mark.parametrize('content,expected', [
    (['6,5,9,4',
      '13,9,10',
      '4,2,3,3',
      '5,3,4,3',
      '1,3,3,2'],
     ([6,5,9,4],
      [13,9,10],
      [[4,2,3,3],
       [5,3,4,3],
       [1,3,3,2]])),
])
def test_rullo_from_csv(content, expected):
    from rullo.rullo import Rullo
    
    f = io.StringIO('\n'.join(content))
    rullo = Rullo.from_csv(f)
    
    assert np.all(rullo.row_constraints == np.array(expected[1]))
    assert np.all(rullo.column_constraints == np.array(expected[0]))
    assert np.all(rullo.content == np.array(expected[2]))
    
    
    