# Committing and pushing

You are now ready to change the code. To do so, open the `src/some_lib/maths.py` file and add the following code (do not change the type hints, we'll do that later!)

```python
def multiply(a: int, b: int) -> int:
    return a * b
```

Commit it with a commit message of your choice.
It's considered good practice to use the imperative mood in the commit message header (the first line) -- this makes them to the point and easy to skim.
For example, a good commit message here could be `Add multiplication function`.

Once you've committed, you should push your changes to your remote repo on GitHub.
To do so, run `git push --set-upstream origin my-branch`.
The first part of this command, `git push`, tells Git to push your changes.
However, since this is a new local branch, you need to tell it where to push it.
We therefore use `set-upstream origin my-branch` to tell Git to use the `origin` remote (where we originally cloned from) and the branch `my-branch`.

Once you've pushed, you're ready to [create a pull request](05-pull-request.md)
