# Introduce java plugin

```
$ gradle build
$ tree
.
├── README.md
├── build
│   ├── classes
│   │   └── java
│   │       └── main
│   │           └── org
│   │               └── gradle
│   │                   └── poetry
│   │                       ├── CrypticPoetry.class
│   │                       └── Poetry.class
│   └── tmp
│       └── compileJava
├── build.gradle
└── src
    └── main
        └── java
            └── org
                └── gradle
                    └── poetry
                        ├── CrypticPoetry.java
                        └── Poetry.java
```

### Execute it in a very pedantic way.
```
$ java -cp build/classes/java/main org.gradle.poetry.Poetry
This is line #1
This is line #2
This is line #3
This is line #4
This is line #5
```

### Execute it in a Gradle way.
```
$ gradle -q caesar
This is line #1
This is line #2
This is line #3
This is line #4
This is line #5

$ gradle -q cC
VGhpcyBpcyBsaW5lICMx
VGhpcyBpcyBsaW5lICMy
VGhpcyBpcyBsaW5lICMz
VGhpcyBpcyBsaW5lICM0
VGhpcyBpcyBsaW5lICM1
```
