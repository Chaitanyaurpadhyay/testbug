import pytest
from calc import divide

def test_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
