#### [How to force “git pull” to overwrite local files](https://stackoverflow.com/questions/1125968/how-do-i-force-git-pull-to-overwrite-local-files)

```
$ git fetch --all && \
  git reset --hard origin/master
```

