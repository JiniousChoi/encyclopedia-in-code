package com.paulbutcher

import akka.actor._

// START:messages
case class Greet(name: String)
case class Praise(name: String)
case class Celebrate(name: String, age: Int)
// END:messages

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

  val talker = system.actorOf(Props[Talker], "talker")

  talker ! Greet("Huey")
  talker ! Praise("Dewey")
  talker ! Celebrate("Louie", 16)

  Thread.sleep(1000)

  system.shutdown
}
// END:main
