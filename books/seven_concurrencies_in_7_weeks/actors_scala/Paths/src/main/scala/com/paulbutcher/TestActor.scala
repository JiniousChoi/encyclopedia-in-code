package com.paulbutcher

import akka.actor._

// START:testactor
case class CreateChild(name: String)
case object SayHello
case class SayHelloFrom(path: String)

class TestActor extends Actor {

  def receive = {
    case CreateChild(name) => context.actorOf(Props[TestActor], name)
    case SayHello => println(s"Hello from $self")
    case SayHelloFrom(path) => context.actorFor(path) ! SayHello
  }
}
// END:testactor