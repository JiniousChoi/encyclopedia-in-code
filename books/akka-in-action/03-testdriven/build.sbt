name := "testdriven"

version := "1.0"

organization := "com.manning"

libraryDependencies ++= {
  val akkaVersion = "2.5.0"
  Seq(
    "com.typesafe.akka"       %%  "akka-actor"   % akkaVersion,
    "com.typesafe.akka"       %%  "akka-slf4j"   % akkaVersion,
    "com.typesafe.akka"       %%  "akka-testkit" % akkaVersion   % "test",
    "org.scalatest"           %%  "scalatest"    % "3.0.1"       % "test"
  )
}
