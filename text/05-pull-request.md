# Pull requests

Pull requests (or merge requests on GitLab) is the process where we request that changes from one branch are incorporated into another branch.
We typically use pull requests to request that changes are incorporated into the main branch of either the current repo or the repo we forked from.
In this case, you should create a pull request from `my-branch` into the `main` branch of the same repo (i.e. you're not requesting that the changes are incorporated upstream).

To create a pull request, navigate to `https://github.com/{{your-username}}/git-learning-by-doing/pulls/` and press the `New pull request` button.
Select `main` as the base branch and `my-branch` as the compare branch, type in some description and title for the pull request press the "Create pull request" button.

You've now created your pull request, let's move on to [modifying it](06-modifying-pr.md).

PS. It's useful to work with branches and pull requests even if we're the only ones working on the repo, they give us a clear overview of all changes made since we branched out and it makes it easier to see if we want to clean up our git commit history (more about that later).
