# Using interactive rebase to change history

As you might have realised, we had the wrong type hints for the multiplication function!
The type hints state that the input is `int`, but it should be `float`.

But oh-no, we have made a commit since we added the multiplication function, so we cannot ammend our previous commit.
In this case, we need to use an [*interactive rebase*](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History).

Rebasing is our main way of changing the Git history, with it we can modify commits, squash them (merge two or more into one), reorder them and much more!

In this case, we'll modify our first commit.
To do so, type `git rebase -i HEAD~2`.
This means that we want start an interactive rebase from one commit before where we are now.

You will now be prompted with the text-editor that Git uses for you, and you will see something like this

```raw
pick 9d4f57e Add multiplication function
pick d82577f Add multiplication tests
```

Pick means that we want to keep that commit without changing it, since we want to modify the code in our first commit, we'll change it so it looks like this instead:

```raw
e 9d4f57e Add multiplication function
pick d82577f Add multiplication tests
```

Save the file and exit the editor.
Git will now start rebasing.
You said that you want to edit the first commit, so Git will "rewind" the code back to that state and allow you to make any edits you wish.

Modify the `src/some_lib/maths.py` file so your type hints state `float` instead of `int`.
Also, have a look at the tests directory to see that there are no `test/maths/test_multiply.py` file.
Why do you think this might be the case?

To finish editing, stage your changes (`git add src/some_lib/maths.py`) and edit your commit (`git commit --amend --no-edit`).
You can now continue the rebasing by running `git rebase --continue`, which will finish the rebasing.

Force push you changes before you move on to [reordering your commits](09-interactive-rebase-reorder.md).

PS. If you had modified the code from the first commit in a later commit, then you'd have to resolve those changes as a standard merge conflict. This can be cumbersome if you have many commits that affect the same lines, since you'd then have to merge these changes for every commit.
