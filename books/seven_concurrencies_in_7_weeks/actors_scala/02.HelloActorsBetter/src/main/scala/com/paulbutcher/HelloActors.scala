package com.paulbutcher

import akka.actor._

// messages
case class Greet(name: String)
case class Praise(name: String)
case class Celebrate(name: String, age: Int)

class Master extends Actor {
  val talker = context.actorOf(Props[Talker], "talker")

  override def preStart {
    context.watch(talker ) // HIGHLIGHT

    talker ! Greet("Huey")
    talker ! Praise("Dewey")
    talker ! Celebrate("Louie", 16)
    talker ! PoisonPill // HIGHLIGHT
  }

  def receive = {
    case Terminated(`talker`) => context.system.terminate()
  }
}

class Talker extends Actor {
  def receive = {
    case Greet(name) => println(s"Hello $name")
    case Praise(name) => println(s"$name, you're amazing")
    case Celebrate(name, age) => println(s"Here's to another $age years, $name")
  }
}

object HelloActors extends App {
  val system = ActorSystem("HelloActors")

  system.actorOf(Props[Master], "master")
}
