# How to run test

## Run all the tests
```console
$ sbt test
[info] Updated file /Users/kakao/github/encyclopedia-in-code/books/akka-in-action/03.chapter-testdriven/project/build.properties: set sbt.version to 1.1.4
[info] Loading settings from idea.sbt ...
[info] Loading global plugins from /Users/kakao/.sbt/1.0/plugins
[info] Loading project definition from /Users/kakao/github/encyclopedia-in-code/books/akka-in-action/03.chapter-testdriven/project
[info] Updating ProjectRef(uri("file:/Users/kakao/github/encyclopedia-in-code/books/akka-in-action/03.chapter-testdriven/project/"), "root-03-chapter-testdriven-build")...
[info] Done updating.
[info] Loading settings from build.sbt,scala.sbt ...
[info] Set current project to testdriven (in build file:/Users/kakao/github/encyclopedia-in-code/books/akka-in-action/03.chapter-testdriven/)
[info] Updating ...
[info] Done updating.
[info] Compiling 1 Scala source to /Users/kakao/github/encyclopedia-in-code/books/akka-in-action/03.chapter-testdriven/target/scala-2.12/classes ...
[info] Non-compiled module 'compiler-bridge_2.12' for Scala 2.12.2. Compiling...
[info]   Compilation completed in 11.293s.
[info] Done compiling.
[info] Compiling 9 Scala sources to /Users/kakao/github/encyclopedia-in-code/books/akka-in-action/03.chapter-testdriven/target/scala-2.12/test-classes ...
[info] Done compiling.
[INFO] [07/16/2018 17:09:37.502] [testsystem-akka.actor.default-dispatcher-2] [akka://testsystem/user/greeter02-1] Hello World!
[info] SilentActor01Test:
[info] A Silent Actor
[info] - must change state when it receives a message, single threaded !!! IGNORED !!!
[info] - must change state when it receives a message, multi-threaded !!! IGNORED !!!
[info] SilentActorTest:
[info] A Silent Actor
[info] - must change internal state when it receives a message, multi
[info] Greeter01Test:
[info] The Greeter
[info] - must say Hello World! when a Greeting("World") is sent to it
[info] SilentActorTest:
[info] A Silent Actor
[info] - must change internal state when it receives a message, single
[info] Greeter02Test:
[info] The Greeter
[info] - must say Hello World! when a Greeting("World") is sent to it
[info] - must say something else and see what happens
[info] EchoActorTest:
[info] An EchoActor
[info] - must Reply with the same message it receives
[info] - must Reply with the same message it receives without ask
[info] SendingActorTest:
[info] A Sending Actor
[info] - must send a message to another actor when it has finished processing
[info] FilteringActorTest:
[info] A Filtering Actor
[info] - must filter out particular messages
[info] - must filter out particular messages using expectNoMsg
[info] Run completed in 9 seconds, 956 milliseconds.
[info] Total number of tests run: 10
[info] Suites: completed 8, aborted 0
[info] Tests: succeeded 10, failed 0, canceled 0, ignored 2, pending 0
[info] All tests passed.
[success] Total time: 26 s, completed Jul 16, 2018 5:09:46 PM
[INFO] [07/16/2018 17:09:46.661] [Thread-7] [CoordinatedShutdown(akka://testsystem)] Starting coordinated shutdown from JVM shutdown hook
```

## Run an individual test
```console
$ sbt
[info] Loading settings from idea.sbt ...
[info] Loading global plugins from /Users/kakao/.sbt/1.0/plugins
[info] Loading project definition from /Users/kakao/github/encyclopedia-in-code/books/akka-in-action/03.chapter-testdriven/project
[info] Loading settings from build.sbt,scala.sbt ...
[info] Set current project to testdriven (in build file:/Users/kakao/github/encyclopedia-in-code/books/akka-in-action/03.chapter-testdriven/)
[info] sbt server started at local:///Users/jinchoi/.sbt/1.0/server/4cf6b86d314eb5038ef8/sock

sbt:testdriven> testOnly aia.testdriven.SilentActor01Test
[info] SilentActor01Test:
[info] A Silent Actor
[info] - must change state when it receives a message, single threaded !!! IGNORED !!!
[info] - must change state when it receives a message, multi-threaded !!! IGNORED !!!
[info] Run completed in 856 milliseconds.
[info] Total number of tests run: 0
[info] Suites: completed 1, aborted 0
[info] Tests: succeeded 0, failed 0, canceled 0, ignored 2, pending 0
[info] No tests were executed.
[success] Total time: 2 s, completed Jul 16, 2018 5:10:41 PM
```
