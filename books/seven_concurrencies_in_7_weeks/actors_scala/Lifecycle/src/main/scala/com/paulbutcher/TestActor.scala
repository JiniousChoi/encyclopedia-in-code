package com.paulbutcher

import akka.actor._

// START:testactor
case class CreateChild(name: String)
case class Divide(x: Int, y: Int)

class TestActor extends Actor {

  def receive = {
    case CreateChild(name) => context.actorOf(Props[TestActor], name)
    case Divide(x, y) => log(s"$x / $y = ${x / y}")
  }

  override def preStart() { log(s"preStart") }

  override def preRestart(reason: Throwable, message: Option[Any]) {
    log(s"preRestart ($reason, $message)")
  }

  override def postRestart(reason: Throwable) { log(s"postRestart ($reason)") }

  override def postStop() { log(s"postStop") }

  def log(message: String) { println(s"${self.path.name}: $message") }
}
// END:testactor