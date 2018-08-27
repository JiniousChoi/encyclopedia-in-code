# how to pass env var to a script-executing environment?

```
jin@jin-VirtualBox:/tmp/test$ ls
all.sh  step1.sh  step2.sh
jin@jin-VirtualBox:/tmp/test$ ./all.sh 
./all.sh: 줄 3: NAME: Name must not be empty
jin@jin-VirtualBox:/tmp/test$ NAME=jin ./all.sh 
Hello 
are you jin?
declare -x LOGNAME="jin"
declare -x NAME="jin"
```

`declare -x` means the variable is exported.
