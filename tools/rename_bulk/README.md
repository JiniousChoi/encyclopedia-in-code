# rename_bulk

## environment

```bash
$ ls -1
video1.avi
video2.avi
video3.avi
subtitle1.smi
subtitle2.smi
subtitle3.smi
```

## usage form 1

### rename_bulk <from.lst> <to.lst>

```bash
$ cat from.lst
subtitle1.smi
subtitle2.smi
subtitle3.smi
```

```bash
$ cat to.lst
video1.smi
video2.smi
video3.smi
```

```bash
$ rename_bulk from.lst to.lst

$ ls -1
video1.avi
video1.smi
video2.avi
video2.smi
video3.avi
video3.smi
```

## usage form 2

### rename_bulk <from.lst> <to.lst> [suffix action ...]
### suffix action := ( -suffix | +suffix )

```bash
$ cat sub.lst
subtitle1.smi
subtitle2.smi
subtitle3.smi
```

```bash
$ cat vid.lst
video1.avi
video2.avi
video3.avi
```

```bash
# '-.avi' right-strips each entry in vid.lst
# '+.smi' append each entry in vid.lst
$ rename_bulk sub.lst vid.lst -.avi +.smi

$ ls -1
video1.avi
video1.smi
video2.avi
video2.smi
video3.avi
video3.smi
```

