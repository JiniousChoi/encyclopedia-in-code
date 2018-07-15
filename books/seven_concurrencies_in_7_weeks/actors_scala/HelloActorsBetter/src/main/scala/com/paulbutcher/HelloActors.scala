package com.paulbutcher

import akka.actor._

// START:messages
case class Greet(name: String)
case class Praise(name: String)
case class Celebrate(name: String, age: Int)
// END:messages

// START:master
class Master extends Actor {

  val talker = context.actorOf(Props[Talker], "talker")

  override def preStart {
    // START_HIGHLIGHT
    context.watch(talker)
    // END_HIGHLIGHT

    talker ! Greet("Huey")
    talker ! Praise("Dewey")
    talker ! Celebrate("Louie", 16)
    // START_HIGHLIGHT
    talker ! PoisonPill
    // END_HIGHLIGHT
  }

  def receive = {
  // START_HIGHLIGHT
    case Terminated(`talker`) => context.system.shutdown
  // END_HIGHLIGHT
  }
}
// END:master

// START:talker
class Talker extends Actor {

  // START:receive
  def receive = {
    case Greet(name) => println(s"Hello $name")
    case Praise(name) => println(s"$name, you're amazing")
    case Celebrate(name, age) => println(s"Here's to another $age years, $name")
  }
  // END:receive
}
// END:talker

// START:main
object HelloActors extends App {

  val system = ActorSystem("HelloActors")

  system.actorOf(Props[Master], "master")
}
// END:main
