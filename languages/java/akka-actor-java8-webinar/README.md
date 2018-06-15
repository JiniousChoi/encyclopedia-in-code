# Reference
https://github.com/johanandren/akka-actor-java8-webinar

# Akka Java 8 Samples
For the Akka with Java 8 JetBrains Webinar 2016-09-13

Dependencies Ver. 1:
* Java 8
* Gradle 
```console
$ gradle init   # assume pom.xml is provided
$ # add tasks for sample 1 to 4
$ ./gradlew sample1
Starting a Gradle Daemon (subsequent builds will be faster)

> Task :sample1
[INFO] [06/15/2018 17:34:29.609] [sample1-akka.actor.default-dispatcher-4] [akka://sample1/user/counter] Increased counter 1
[INFO] [06/15/2018 17:34:29.609] [sample1-akka.actor.default-dispatcher-4] [akka://sample1/user/counter] Increased counter 2
[INFO] [06/15/2018 17:34:29.609] [sample1-akka.actor.default-dispatcher-4] [akka://sample1/user/counter] Increased counter 3
[INFO] [06/15/2018 17:34:29.609] [sample1-akka.actor.default-dispatcher-4] [akka://sample1/user/counter] Increased counter 4
[INFO] [06/15/2018 17:34:29.609] [sample1-akka.actor.default-dispatcher-4] [akka://sample1/user/counter] Increased counter 5
[INFO] [06/15/2018 17:34:29.610] [sample1-akka.actor.default-dispatcher-4] [akka://sample1/user/counter] Increased counter 6
[INFO] [06/15/2018 17:34:29.610] [sample1-akka.actor.default-dispatcher-4] [akka://sample1/user/counter] Increased counter 7
[INFO] [06/15/2018 17:34:29.610] [sample1-akka.actor.default-dispatcher-4] [akka://sample1/user/counter] Increased counter 8
[INFO] [06/15/2018 17:34:29.610] [sample1-akka.actor.default-dispatcher-4] [akka://sample1/user/counter] Increased counter 9
...(omit)...
```

Dependencies Ver. 2:
* Java 8
* Maven 3
```console
$ mvn install
$ # you could use maven plugin for executing java main class
$ # refer to https://stackoverflow.com/questions/9846046/run-main-class-of-maven-project
$ java -cp target/classes:/Users/kakao/.m2/repository/com/typesafe/akka/akka-actor_2.11/2.4.9/akka-actor_2.11-2.4.9.jar:/Users/kakao/.m2/repository/com/typesafe/akka/akka-http-core_2.11/2.4.9/akka-http-core_2.11-2.4.9.jar:/Users/kakao/.m2/repository/com/typesafe/akka/akka-http-experimental_2.11/2.4.9/akka-http-experimental_2.11-2.4.9.jar:/Users/kakao/.m2/repository/com/typesafe/akka/akka-http-jackson-experimental_2.11/2.4.9/akka-http-jackson-experimental_2.11-2.4.9.jar:/Users/kakao/.m2/repository/com/typesafe/akka/akka-parsing_2.11/2.4.9/akka-parsing_2.11-2.4.9.jar:/Users/kakao/.m2/repository/com/typesafe/akka/akka-stream_2.11/2.4.9/akka-stream_2.11-2.4.9.jar:/Users/kakao/.m2/repository/com/typesafe/akka/akka-testkit_2.11/2.4.9/akka-testkit_2.11-2.4.9.jar:/Users/kakao/.m2/repository/org/scala-lang/modules/scala-java8-compat_2.11/0.7.0/scala-java8-compat_2.11-0.7.0.jar:/Users/kakao/.m2/repository/org/scala-lang//modules/scala-java8-compat_2.11/0.7.0/scala-java8-compat_2.11-0.7.0.jar:/Users/kakao/.m2/repository/org/scala-lang//modules/scala-parser-combinators_2.11/1.0.4/scala-parser-combinators_2.11-1.0.4.jar:/Users/kakao/.m2/repository/org/scala-lang//scala-library/2.11.8/scala-library-2.11.8.jar:/Users/kakao/.m2/repository/com/typesafe/config//1.3.0/config-1.3.0.jar com.lightbend.akkasample.sample1.App
```
