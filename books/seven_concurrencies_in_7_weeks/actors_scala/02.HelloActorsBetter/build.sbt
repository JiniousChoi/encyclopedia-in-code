organization := "com.paulbutcher"

name := "actors-hello-actors-better"

version := "1.0"

scalaVersion := "2.12.0"

scalacOptions ++= Seq("-deprecation", "-unchecked", "-feature")

libraryDependencies += "com.typesafe.akka" %% "akka-actor" % "2.5.0"
