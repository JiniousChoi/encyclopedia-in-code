## [parameter expansion](https://www.gnu.org/software/bash/manual/bashref.html#Shell-Parameter-Expansion)
```bash
$ ${NAME:=jin}  # is totally same as ${NAME=jin}
-bash: jin: command not found
$ echo $NAME
jin
```

## [colon operator (no-op)](https://www.gnu.org/software/bash/manual/bashref.html#Bourne-Shell-Builtins)
```bash
$ : ${AGE:=18}
$ echo $AGE
18
```
