## /usr/bin/stat
### In order to determine the three files that have been modified/created/accessed most recently,
```console
$ stat -f "%Sm %N" /tmp/* | sort -rn | head -3
Jun 20 10:03:18 2018 /tmp/symc00001dbe
Jun 20 10:00:44 2018 /tmp/symc00001d82
Jun 20 08:06:47 2018 /tmp/symc00001cb7

$ stat -f "%Sc %N" /tmp/* | sort -rn | head -3
Jun 20 11:23:26 2018 /tmp/registry.lock
Jun 20 10:03:18 2018 /tmp/symc00001dbe
Jun 20 10:00:44 2018 /tmp/symc00001d82

$ stat -f "%Sa %N" /tmp/* | sort -rn | head -3
Jun 20 10:45:40 2018 /tmp/com.apple.launchd.YGuHVqj18L
Jun 20 10:45:40 2018 /tmp/com.apple.launchd.VJEMgX6OPc
Jun 20 10:45:40 2018 /tmp/AVScanfclC
```

## /bin/expr
### matching by group
this prints firstly-matched string in the parenthesis
```
$ ls=$(ls -ld $(which python3))
$ echo $ls
lrwxr-xr-x  1 kakao  admin  34 Apr  4 16:25 /usr/local/bin/python3 -> ../Cellar/python/3.6.5/bin/python3
$ expr "$ls" : '.*-> \(.*\)$'
../Cellar/python/3.6.5/bin/python3
```

## /etc/*-release in linux server
this shows what linux distribution it is
```console
# ls /etc/*release
/etc/alpine-release  /etc/os-release

# cat /etc/alpine-release 
3.7.0

# cat /etc/os-release 
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.7.0
PRETTY_NAME="Alpine Linux v3.7"
HOME_URL="http://alpinelinux.org"
BUG_REPORT_URL="http://bugs.alpinelinux.org"
```

## [/usr/bin/xargs](https://stackoverflow.com/questions/35589179/when-to-use-xargs-when-piping)
Virtually, it transforms(X) standard input as arguments(ARGS), hence the name `XARGS`.
`printf` utility does NOT read standard input. It uses given arguments.
```
jinchoi$ cat auth.guest 
23bc46b1-71f6-4ed5-8c54-816aa4f8c502:123zO3xZCLrMN6v2BKK1dXYFpXlPkccOFqm12CdAsMgRU4VrNZ9lyGVCGuMDGIwPjinchoi$ 
```
```
jinchoi$ cat auth.guest | printf "%s\n"

jinchoi$
```
```
jinchoi$ cat auth.guest | xargs printf "%s\n"
23bc46b1-71f6-4ed5-8c54-816aa4f8c502:123zO3xZCLrMN6v2BKK1dXYFpXlPkccOFqm12CdAsMgRU4VrNZ9lyGVCGuMDGIwP
jinchoi$ 
```

# todo
https://unix.stackexchange.com/questions/16443/combine-text-files-column-wise
