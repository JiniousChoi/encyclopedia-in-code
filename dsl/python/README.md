# Writing a Simple (internal) DSL in Python

## Structure and Samples 
```console
$ tree
.
├── dsl_parser.py
├── modules
│   ├── module1.py
│   └── module2.py
├── src1.dsl
└── src2.dsl

$ cat src1.dsl
module1 add 1 2

$ ./dsl_parser.py src1.dsl 
3

$ cat src2.dsl
module2 add_str foo bar baz debug=1 trace=0
module2 add_num 1 2 3 4 5 6 7 8 9 10
module2 add_num 1 2 3 type=int
module2 add_num 1 2 3.0 type=float

$ ./dsl_parser.py src2.dsl 
foobarbaz debug=1,trace=0
55
6
6.0
```

### Reference
https://github.com/natej/dsl
