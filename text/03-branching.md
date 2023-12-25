## Branching

One of the most useful features of Git is [branches](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell).
Branches are a very neat way to keep track of multiple versions of the code at once.
For example, the main branch should ideally only consist of working commits, so all unittests and linter checks should pass for all commits on the main branch.
However, when we are developing the code, we want to incrementally change the code and potentially break something that we fix at a later point.
To keep track of both the working version of the code and the development version, we use branches.

To create and switch to the new branch, type `git switch -c my-branch` (or `git checkout -b my-branch`).
This tells Git to switch to create the branch `my-branch` and switch to it (if you want to switch between existing branches, use `git switch my-branch` or `git checkout my-branch`).

You can now move on to [making and pushing changes](04-pushing.md)

PS. `git switch` and `git checkout` are very similar commands.`git checkout` can do the the same as `git switch`, but it can also do other things. Therefore, the Git developers introduced the `switch`command to avoid confusion (see [this StackOverflow answer](https://stackoverflow.com/a/57266005) for more information).
