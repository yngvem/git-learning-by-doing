# Reordering commits

Sometimes, it can be useful to reorder your commits.
A particularly common example is if you want to merge two commits, but there is an unrelated commit inbetween those two.
Since Git can only merge subsequent commits (more on that later), you first have to re-order them.

In our case, it doesn't make much sense to reorder the commits, but it can still be useful to have practiced it.

To change the order of your commits, do an interactive rebase with the last two commits.
Again, this should give you a text editor with something like this:

```raw
pick 123...
pick 456...
```

We want to re-order them so commit `TODO 456` comes before commit `TODO123` in the commit log.
To do this, we simply reorder the lines in our text editor:

```raw
pick 456...
pick 123...
```

Save and exit the editor, and Git will re-order your changes for you.
To double-check this, run `git log` to see the commit history.

You are now ready to learn about [stashing](10-stashing.md).
