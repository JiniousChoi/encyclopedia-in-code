package com.paulbutcher

import akka.actor._
import akka.routing.{Broadcast, RoundRobinRouter}

// START:master
class Master extends Actor {

  val accumulator = context.actorOf(Props[Accumulator], "accumulator")
  val counters = context.actorOf(
    // START_HIGHLIGHT
    Props(new Counter(accumulator)).withRouter(RoundRobinRouter(4)),
    // END_HIGHLIGHT
    "counter")
  val parser = context.actorOf(Props(new Parser(counters)), "parser")

  override def preStart {
    context.watch(accumulator)
    context.watch(counters)
    context.watch(parser)
  }

  def receive = {
    // START_HIGHLIGHT
    case Terminated(`parser`) => counters ! Broadcast(PoisonPill)
    // END_HIGHLIGHT
    case Terminated(`counters`) => accumulator ! PoisonPill
    case Terminated(`accumulator`) => context.system.shutdown
  }
}
// END:master