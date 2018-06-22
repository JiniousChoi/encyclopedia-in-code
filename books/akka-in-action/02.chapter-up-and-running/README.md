## sbt assembly
compile and then package into a jar

```console
$ sbt assembly
[warn] Executing in batch mode.
[warn]   For better performance, hit [ENTER] to switch to interactive mode, or
[warn]   consider launching sbt without any commands, or explicitly passing 'shell'
[info] Loading project definition from /Users/jinchoi/github/encyclopedia-in-code/books/akka-gilbut/02.chapter-up-and-running/project
[info] Updating {file:/Users/jinchoi/github/encyclopedia-in-code/books/akka-gilbut/02.chapter-up-and-running/project/}root-02-chapter-up-and-running-build...
[info] Resolving org.fusesource.jansi#jansi;1.4 ...
[info] Done updating.
[info] Set current project to goticks (in build file:/Users/jinchoi/github/encyclopedia-in-code/books/akka-gilbut/02.chapter-up-and-running/)
[info] Updating {file:/Users/jinchoi/github/encyclopedia-in-code/books/akka-gilbut/02.chapter-up-and-running/}root-02-chapter-up-and-running...
[info] Resolving jline#jline;2.14.3 ...
[info] Done updating.
[warn] There may be incompatibilities among your library dependencies.
[warn] Here are some of the libraries that were evicted:
[warn] 	* com.typesafe.akka:akka-stream_2.12:2.4.17 -> 2.5.0
[warn] 	* com.typesafe.akka:akka-actor_2.12:2.4.17 -> 2.5.0
[warn] Run 'evicted' to see detailed eviction warnings
[info] Compiling 5 Scala sources to /Users/jinchoi/github/encyclopedia-in-code/books/akka-gilbut/02.chapter-up-and-running/target/scala-2.12/classes...
[info] Compiling 3 Scala sources to /Users/jinchoi/github/encyclopedia-in-code/books/akka-gilbut/02.chapter-up-and-running/target/scala-2.12/test-classes...
[info] Including: ssl-config-core_2.12-0.2.1.jar
[info] Including: spray-json_2.12-1.3.3.jar
[info] Including: config-1.3.1.jar
[info] Including: scala-java8-compat_2.12-0.8.0.jar
[info] Including: akka-actor_2.12-2.5.0.jar
[info] Including: akka-stream_2.12-2.5.0.jar
[info] Including: akka-http-core_2.12-10.0.5.jar
[info] Including: scala-library-2.12.2.jar
[info] Including: scala-parser-combinators_2.12-1.0.4.jar
[info] Including: akka-slf4j_2.12-2.5.0.jar
[info] Including: logback-classic-1.2.3.jar
[info] Including: akka-http_2.12-10.0.5.jar
[info] Including: logback-core-1.2.3.jar
[info] Including: reactive-streams-1.0.0.jar
[info] Including: akka-http-spray-json_2.12-10.0.5.jar
[info] Including: akka-parsing_2.12-10.0.5.jar
[info] Including: slf4j-api-1.7.25.jar
[info] TickerSellerSpec:
[info] The TicketSeller
[info] - must Sell tickets until they are sold out
[info] - must Sell tickets in batches until they are sold out
[info] BoxOfficeSpec:
[info] The BoxOffice
[info] - must Create an event and get tickets from the correct Ticket Seller
[info] - must Create a child actor when an event is created and sends it a Tickets message
[info] - must Get and cancel an event that is not created yet
[info] - must Cancel a ticket which event is not created 
[info] - must Cancel a ticket which event is created
[info] Run completed in 1 second, 213 milliseconds.
[info] Total number of tests run: 7
[info] Suites: completed 2, aborted 0
[info] Tests: succeeded 7, failed 0, canceled 0, ignored 0, pending 0
[info] All tests passed.
[info] Checking every *.class/*.jar file's SHA-1.
[info] Merging files...
[warn] Merging 'META-INF/MANIFEST.MF' with strategy 'discard'
[warn] Merging 'META-INF/maven/ch.qos.logback/logback-classic/pom.properties' with strategy 'discard'
[warn] Merging 'META-INF/maven/ch.qos.logback/logback-classic/pom.xml' with strategy 'discard'
[warn] Merging 'META-INF/maven/ch.qos.logback/logback-core/pom.properties' with strategy 'discard'
[warn] Merging 'META-INF/maven/ch.qos.logback/logback-core/pom.xml' with strategy 'discard'
[warn] Merging 'META-INF/maven/org.slf4j/slf4j-api/pom.properties' with strategy 'discard'
[warn] Merging 'META-INF/maven/org.slf4j/slf4j-api/pom.xml' with strategy 'discard'
[warn] Merging 'reference.conf' with strategy 'concat'
[warn] Strategy 'concat' was applied to a file
[warn] Strategy 'discard' was applied to 7 files
[info] SHA-1: 9b6f6684e4423db560ca4bf9c33025def7949a8b
[info] Packaging /Users/jinchoi/github/encyclopedia-in-code/books/akka-gilbut/02.chapter-up-and-running/target/scala-2.12/goticks-assembly-1.0.jar ...
[info] Done packaging.
[success] Total time: 19 s, completed Jun 22, 2018 10:28:29 AM
```

## start akka-http server

```console
$ java -jar ./target/scala-2.12/goticks-assembly-1.0.jar 
INFO  [Slf4jLogger]: Slf4jLogger started
INFO  [go-ticks]: RestApi bound to /0:0:0:0:0:0:0:0:5000
...

$ sbt run
[warn] Executing in batch mode.
[warn]   For better performance, hit [ENTER] to switch to interactive mode, or
[warn]   consider launching sbt without any commands, or explicitly passing 'shell'
[info] Loading project definition from /Users/jinchoi/github/encyclopedia-in-code/books/akka-gilbut/02.chapter-up-and-running/project
[info] Set current project to goticks (in build file:/Users/jinchoi/github/encyclopedia-in-code/books/akka-gilbut/02.chapter-up-and-running/)
[info] Running com.goticks.Main 
INFO  [Slf4jLogger]: Slf4jLogger started
INFO  [go-ticks]: RestApi bound to /0:0:0:0:0:0:0:0:5000 

```

## run test

```console
$ sbt clean compile test
[warn] Executing in batch mode.
[warn]   For better performance, hit [ENTER] to switch to interactive mode, or
[warn]   consider launching sbt without any commands, or explicitly passing 'shell'
[info] Loading project definition from /Users/jinchoi/github/encyclopedia-in-code/books/akka-gilbut/02.chapter-up-and-running/project
[info] Set current project to goticks (in build file:/Users/jinchoi/github/encyclopedia-in-code/books/akka-gilbut/02.chapter-up-and-running/)
[success] Total time: 1 s, completed Jun 22, 2018 10:34:51 AM
[info] Updating {file:/Users/jinchoi/github/encyclopedia-in-code/books/akka-gilbut/02.chapter-up-and-running/}root-02-chapter-up-and-running...
[info] Resolving jline#jline;2.14.3 ...
[info] Done updating.
[warn] There may be incompatibilities among your library dependencies.
[warn] Here are some of the libraries that were evicted:
[warn] 	* com.typesafe.akka:akka-stream_2.12:2.4.17 -> 2.5.0
[warn] 	* com.typesafe.akka:akka-actor_2.12:2.4.17 -> 2.5.0
[warn] Run 'evicted' to see detailed eviction warnings
[info] Compiling 5 Scala sources to /Users/jinchoi/github/encyclopedia-in-code/books/akka-gilbut/02.chapter-up-and-running/target/scala-2.12/classes...
[success] Total time: 9 s, completed Jun 22, 2018 10:35:01 AM
[info] Compiling 3 Scala sources to /Users/jinchoi/github/encyclopedia-in-code/books/akka-gilbut/02.chapter-up-and-running/target/scala-2.12/test-classes...
[info] BoxOfficeSpec:
[info] The BoxOffice
[info] - must Create an event and get tickets from the correct Ticket Seller
[info] - must Create a child actor when an event is created and sends it a Tickets message
[info] - must Get and cancel an event that is not created yet
[info] - must Cancel a ticket which event is not created 
[info] - must Cancel a ticket which event is created
[info] TickerSellerSpec:
[info] The TicketSeller
[info] - must Sell tickets until they are sold out
[info] - must Sell tickets in batches until they are sold out
[info] Run completed in 724 milliseconds.
[info] Total number of tests run: 7
[info] Suites: completed 2, aborted 0
[info] Tests: succeeded 7, failed 0, canceled 0, ignored 0, pending 0
[info] All tests passed.
[success] Total time: 3 s, completed Jun 22, 2018 10:35:04 AM
```

## REST API

| desc | http verb | url | request body | http status | response e.g |
| ---- | --------- | --- | ------------ | ----------- | ------------ |
| create event | POST | /events/RHCP | {"tickets":250} | 201 Created | {"name" : "RHCP",<br/>"tickets" : 250} |
| list event | GET | /events/ | | 200 OK | [ {"event":"RHCP",<br/>{"tickets":249},<br/>{"event":"Radiohead"},<br/>{"tickets":130} ] |
| buy ticket | POST | /events/RHCP/tickets | {"tickets":2} | 201 Created | {"event":"RHCP",<br/>"entries":[{"id":1},{"id":2}]} |
| cancel event | DELETE | /events/RHCP | | 200 OK | {"event":"RHCP",<br/>"tickets":249} |

## create event
```console
# brew install httpie`
```

```console
$ http POST localhost:5000/events/RHCP tickets:=10
HTTP/1.1 201 Created
Content-Length: 28
Content-Type: application/json
Date: Fri, 22 Jun 2018 02:11:36 GMT
Server: GoTicks.com REST API

{
    "name": "RHCP",
    "tickets": 10
}

$ http POST localhost:5000/events/DJMadlib tickets:=15
HTTP/1.1 201 Created
Content-Length: 32
Content-Type: application/json
Date: Fri, 22 Jun 2018 02:17:42 GMT
Server: GoTicks.com REST API

{
    "name": "DJMadlib",
    "tickets": 15
}
```

## list events
```console
$ http GET localhost:5000/events
HTTP/1.1 200 OK
Content-Length: 73
Content-Type: application/json
Date: Fri, 22 Jun 2018 02:18:18 GMT
Server: GoTicks.com REST API

{
    "events": [
        {
            "name": "DJMadlib",
            "tickets": 15
        },
        {
            "name": "RHCP",
            "tickets": 8
        }
    ]
}
```

## buy two tickets for RHCP
```console
$ http POST localhost:5000/events/RHCP/tickets tickets:=2
HTTP/1.1 201 Created
Content-Length: 46
Content-Type: application/json
Date: Fri, 22 Jun 2018 02:19:13 GMT
Server: GoTicks.com REST API

{
    "entries": [
        {
            "id": 1
        },
        {
            "id": 2
        }
    ],
    "event": "RHCP"
}

$ http GET localhost:5000/events
HTTP/1.1 200 OK
Content-Length: 73
Content-Type: application/json
Date: Fri, 22 Jun 2018 02:19:25 GMT
Server: GoTicks.com REST API

{
    "events": [
        {
            "name": "DJMadlib",
            "tickets": 15
        },
        {
            "name": "RHCP",
            "tickets": 8
        }
    ]
}
```

## when trying to buy more tickets than available
```console
$ http POST localhost:5000/events/RHCP/tickets tickets:=1000
HTTP/1.1 404 Not Found
Content-Length: 83
Content-Type: text/plain; charset=UTF-8
Date: Fri, 22 Jun 2018 02:22:58 GMT
Server: GoTicks.com REST API

The requested resource could not be found but may be available again in the future.
```

Heroku deployment
=================

Heroku normally expects the project to reside in the root of the git repo.
the source code for the up and running chapter is not in the root of the repo, so you need to use a different command to deploy to heroku:

    git subtree push --prefix chapter-up-and-running heroku master

This command has to be executed from the root of the git repo, not from within the chapter directory.
The git subtree command is not as featured as the normal push command, for instance, it does not provide a flag to force push,
and it does not support the <local-branch>:<remote-branch> syntax which you can use with git push:

    git push heroku my-localbranch:master

Which is normally used to deploy from a branch to heroku (pushing a branch to heroku master).
It is possible to nest commands though, so if you want to push from a branch you can do the following:

    git push heroku `git subtree split --prefix chapter-up-and-running my-local-branch`:master

Where *my-local-branch* is your local branch.
Forcing a push can be done by nesting commands as well:

    git push heroku `git subtree split --prefix chapter-up-and-running master`:master --force

The above pushes the changes in local master to heroku master.
