# Linux Commands by Examples

## /usr/bin/dirname
```
$ dirname /usr/bin/  
/usr  
  
$ dirname dir1/str dir2/str  
dir1  
dir2  
  
$ dirname stdio.h  
.  
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


