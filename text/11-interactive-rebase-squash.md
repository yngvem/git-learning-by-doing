# Squashing commits

We're now almost ready to merge our pull request.
However, we have multiple commits, and to make the Git log as readable as possible, it's common to make sure that each commit represents one complete code change.
This means that each commit should contain new unit tests (for features) or regression tests (for bug fixes).

However, a new feature might consist of multiple complete code changes, so it can still be (and often is) useful with multiple commits in the same branch.
Rebasing is therefore an extremely useful skill.
By rebasing, we can commit often to begin with, not really caring if we have added all tests or if what we've finished constitutes a "complete code change".
Then, once we have finished whatever we are working on, we can reorder the commits so related commits are grouped together other before we "merge" them together (known as *squashing*) into just a few commits, each representing a complete code change.

You should know squash all your commits into one.
To do that, do an interactive rebase `git rebase -i HEAD~3` and select `s` for the two latest commits:

```raw
pick 1991
s 129012
s 192103
```

As usual, save and exit the code editor.
You will now be promted with a new editor to type in your new commit message.
Something along the lines of "Add multiplication function" will be appropriate.
You can now force push your changes before you navigate to the PR and check that it now consists of only one commit.

You can now merge the PR and be happy that you completed these exercises 🎉
