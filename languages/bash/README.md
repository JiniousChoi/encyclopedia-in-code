# [parameter expansion](https://www.gnu.org/software/bash/manual/bashref.html#Shell-Parameter-Expansion)


## `${parameter:=word}` - Assign Default Value
```bash
$ ${NAME:=jin}  # is totally same as ${NAME=jin}
-bash: jin: command not found
$ echo $NAME
jin
```

using with `:` operator
```bash
$ : ${AGE:=18}
$ echo $AGE
18
```


## `${parameter:?word}` - Display Error if Null or Unset

(man bash) Display Error if Null or Unset. If parameter is null or unset, the expansion of word (or a message to that effect if word is not present) is written to the standard error and the shell, if it is not interactive, exits. Otherwise, the value of parameter is substituted.

```bash
$ : ${NAME:?"NAME must be set and non-empty"}
-bash: NAME: NAME must be set and non-empty
```

```bash
$ NAME=jin
$ : ${NAME:?"NAME must be set and non-empty"}
$ 
```


# Reference

## [colon operator (no-op)](https://www.gnu.org/software/bash/manual/bashref.html#Bourne-Shell-Builtins)
