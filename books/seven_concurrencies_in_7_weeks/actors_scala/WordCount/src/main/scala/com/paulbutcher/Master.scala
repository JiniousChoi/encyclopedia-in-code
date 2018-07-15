package com.paulbutcher

import akka.actor._

// START:master
class Master extends Actor {

  val counter = context.actorOf(Props[Counter], "counter")
  val parser = context.actorOf(Props(new Parser(counter)), "parser")

  override def preStart {
    context.watch(counter)
    context.watch(parser)
  }

  def receive = {
    case Terminated(`parser`) => counter ! PoisonPill
    case Terminated(`counter`) => context.system.shutdown
  }
}
// END:master