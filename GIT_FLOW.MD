>>
>>
>> git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        GIT_HELP.MD

nothing added to commit but untracked files present (use "git add" to track)
>>
>>
>> git add .\GIT_HELP.MD
>>
>>
>> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   GIT_HELP.MD

>>
>>
>> git commit -m "first commit"
[main b47c655] first commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 GIT_HELP.MD
>>
>>
>> git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
>>
>>
>> git push
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 289 bytes | 289.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To github.com:****/****.git
   b27780e..b47c655  main -> main
