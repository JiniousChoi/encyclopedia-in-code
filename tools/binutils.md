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

# todo
https://unix.stackexchange.com/questions/16443/combine-text-files-column-wise
