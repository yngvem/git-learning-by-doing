# Stashing changes

You cannot do an interactive rebase when you have uncommitted changes to tracked files.
However, you might not have any changes that you want to commit yet, but you also don't want to delete your changes.
The obvious way around this is to commit your changes, do the rebase and at the end do a [mixed reset](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified) to undo the latest commit.
However, while that approach works, Git provides us with a tool specifically for these sorts of actions: [the stash](https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning).

We won't go into details on the stash here, only the two most useful features (to me at least).
To see it in action, start by adding the following code to `tests/maths/test_multiply.py` **WITHOUT COMMITTING**

```python
@pytest.mark.parametrize("x", [-1, 0, 1, 3.1416, -3.1416])
def test_multiply_by_zero(x: float) -> None:
    assert some_lib.maths.multiply(x, 0) == 0
```

Now, let's try to do an interactive rebase again: `git rebase -i HEAD~2`.
You should now be met with the following error message:

```raw
error: cannot rebase: You have unstaged changes.
error: Please commit or stash them.
```

As we see, we cannot do the rebase while we have uncommitted changes.
To fix this, we can add our current changes to the stash.
This essentially means that we create a commit, but it's not on the branch, we're currently working on.
Instead, the commit is added to the stash, so it will look as if we undid our changes.
To see this in action, run `git stash` before you open the `tests/maths/test_multiply.py`.
You should now see that our new test is gone!

To get your test back, run `git stash pop` which will take the latest code stashed off the stash and apply them to our files (but not commit anything). Open the `tests/maths/test_multiply.py` again to see.

Make a new commit (with a message along the lines of `Add new multiplication test`) before you move on to the final topic: [squashing commits](11-interactive-rebase-squash.md).
