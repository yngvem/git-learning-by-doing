# Modifying a pull request

After creating the pull request, we realise that we forgot to add tests to the code we added.
Create a new file: `tests/maths/test_multiply.py` and add the following code:

```python
import pytest

import some_lib.maths


@pytest.mark.parametrize("x", [-1, 0, 1, 3.1416, -3.1416])
@pytest.mark.parametrize("y", [-1, 0, 1, 3.1416, -3.1416])
def test_commutative(x: float, y: float) -> None:
    assert some_lib.maths.multiply(x, y) == some_lib.maths.multiply(y, x)
```

Create a new commit this test before you use `git push` to push it. Have a look at the pull request you created, it should now be updated with the new commit!

You are now ready to [modify the previous commit](07-ammending-commits.md).
