# Ammending commits

Let's expand with more tests! Add the following code to the `tests/maths/test_multiply.py` file:

```python
@pytest.mark.parametrize("x", [-1, 0, 1, 3.1416, -3.1416])
def test_one_identity(x: float) -> None:
    assert some_lib.maths.multiply(x, 1) == x
```

Stage this file with `git add tests/maths/test_multiply.py` and run the command `git commit --amend --no-edit`.
This will modify the previous commit (`--amend`) without modifying the commit message (`--no-edit`).

Have a look at the log (run `git log`), to see that there are no new commits.
This is because instead of adding a new commit, you modified the previous one.
Modifying commits like this is an important skill when you get better at coding -- it's what makes it possible to have a clear and understandable changelog.

However, if you try to push these changes to the remote repository, you'll get an error stating **TODO ERROR MESSAGE**.
The reason you get this error is that your commit history is different from the one online.
So Git thinks you're lacking a commit that's available on GitHub.
However, this is not the case, so we need to force GitHub to accept our changes, which is known as a *force push*.
To push your changes, run `git push --force`.

Next we'll look at some more advanced Git editing known as [interactive rebasing](08-interactive-rebase-edit.md).
