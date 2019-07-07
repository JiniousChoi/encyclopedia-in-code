# SICP

## Environment

```
$ docker pull nacyot/scheme-guile
```

```
$ docker run --rm -i -t -v $(pwd):/source nacyot/scheme-guile:apt guile -V
guile (GNU Guile) 2.0.9
Copyright (C) 2013 Free Software Foundation, Inc.

License LGPLv3+: GNU LGPL 3 or later <http:>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
```

```
$ docker run --rm -i -t -v $(pwd)/source:/source nacyot/scheme-guile:apt guile /source/helloworld.scm
Hello, World!
```

```
$ docker run --rm -i -t nacyot/scheme-guile:apt guile
GNU Guile 2.0.9
Copyright (C) 1995-2013 Free Software Foundation, Inc.

Guile comes with ABSOLUTELY NO WARRANTY; for details type `,show w'.
This program is free software, and you are welcome to redistribute it
under certain conditions; type `,show c' for details.

Enter `,help' for help.
scheme@(guile-user)> 
```
