# linux commands and configs

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


## /usr/bin/dirname
```
$ dirname /usr/bin/  
/usr  
  
$ dirname dir1/str dir2/str  
dir1  
dir2  

$ dirname stdio.h  
. # meaning the current directory
```


## /usr/bin/basename
```
$ basename /usr/bin/sort  
sort  
  
$ basename include/stdio.h .h  
stdio  
  
$ basename -s .h include/stdio.h  
stdio  
  
$ basename -a any/str1 any/str2  
str1  
str2  
  
$ basename -s .h -a path/file1.h path/file2.h  
file1  
file2  
```


## /bin/lsblk
### list block devices

disk of IDE/SATA/SCSI type
```
jin@pm01:~$ lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda      8:0    0  79.4G  0 disk 
|-sda1   8:1    0    30M  0 part 
|-sda2   8:2    0   477M  0 part /boot
|-sda3   8:3    0   9.6G  0 part [SWAP]
`-sda4   8:4    0  69.4G  0 part /
```

[disk type of the paravirtualizated](https://serverfault.com/a/803391)
```
jin@vm01:~$ lsblk
NAME   MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
vda    253:0    0  50G  0 disk 
`-vda1 253:1    0  50G  0 part /
```


## /bin/stty - set the options for a terminal device interface

#### [How to reverse-i-search back and forth?](https://stackoverflow.com/questions/12373586/how-to-reverse-i-search-back-and-forth)

`stty -ixon` enables <C-s> for forward-i-search, whereas <C-r> is for reverse-i-search.


## /usr/bin/bluetoothctl
How to connect to bluetooth speak automatically on booting

```
$ cat /etc/rc.local
...
echo "connect 00:02:3C:4C:B2:A8" | bluetoothctl
...
```


## /usr/bin/pacmd
Reconfigure a PulseAudio sound server during runtime

```
$ cat /etc/rc.local
...
pacmd set-default-sink bluez_sink.00_02_3C_4C_B2_A8 >> /etc/rc.local
...
```
```
$ pacmd stat
...
Default sink name: bluez_sink.00_02_3C_4C_B2_A8
Default source name: alsa_input.pci-0000_00_1b.0.analog-stereo
...
```


## How to use proxy on linux server

### set proxy for the current shell

```
$ unset http_proxy
$ unset https_proxy
$ export http_proxy=http://proxy.example.com:3128
$ export https_proxy=http://proxy.example.com:3128
```

### `sudo apt-get update` doesn't work?

`sudo` opens a new shell environment. A workaround is to preserve the environment variable,

```
sudo -E apt-get update
```

### `./gradlew` fails on downloading `gradle-?.?.?-bin.zip`

- set jvm options in gradlew
  ```
  $ cat ./gradlew
  ...
  # Add default JVM options here. You can also use JAVA_OPTS and GRADLE_OPTS to pass JVM options to this script.
  DEFAULT_JVM_OPTS="-Dhttp.proxyHost=proxy.example.com -Dhttp.proxyPort=3128 -Dhttps.proxyHost=proxy.example.com -Dhttps.proxyPort=3128"
  ...
  ```
- [set global proxy setting](https://stackoverflow.com/questions/34640698/gradle-failing-to-download-distribution-behind-company-proxy)
  ```
  $ cat ~/.gradle/gradle.properties
  org.gradle.daemon=true
  systemProp.https.proxyHost=proxy.example.com
  systemProp.https.proxyPort=3128
  systemProp.http.proxyHost=proxy.example.com
  systemProp.http.proxyPort=3128
  systemProp.https.nonProxyHosts=*.example.com|localhost
  ```
  this is like passing these args to gradlew, say, `./gradlew -Dhttp.proxyHost=xxx -Dhttp.proxyPort=xxx -Dhttps.proxyHost=xxx -Dhttps.proxyPort=xxx`


## /usr/sbin/usermod

#### append a user to a group
```
# after installing docker
$ sudo usermod -a -G docker $USER
```

#### You need to log back in.
```
$ groups
jin adm cdrom sudo dip plugdev lpadmin sambashare
$ docker ps
Cannot connect to the Docker daemon. Is the docker daemon running on this host?
```

#### Ad-hoc
```
$ sudo su $USER -c 'groups'
jin adm cdrom sudo dip plugdev lpadmin sambashare docker
$ sudo su $USER -c 'docker ps'
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

#### Limitation: Not working for every situations
```
jin@jin-VirtualBox:~/github/openwhisk$ sudo su $USER -c './gradlew distDocker' 2>&1 | head
Cannot connect to the Docker daemon. Is the docker daemon running on this host?
...
```


# todo
https://unix.stackexchange.com/questions/16443/combine-text-files-column-wise

