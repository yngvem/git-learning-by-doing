import pytest

import some_lib.maths


@pytest.mark.parametrize("x", [-1, 0, 1, 3.1416, -3.1416])
@pytest.mark.parametrize("y", [-1, 0, 1, 3.1416, -3.1416])
def test_commutative(x: float, y: float) -> None:
    assert some_lib.maths.add(x, y) == some_lib.maths.add(y, x)


@pytest.mark.parametrize("x", [-1, 0, 1, 3.1416, -3.1416])
def test_zero_identity(x: float) -> None:
    assert some_lib.maths.add(x, 0) == x
