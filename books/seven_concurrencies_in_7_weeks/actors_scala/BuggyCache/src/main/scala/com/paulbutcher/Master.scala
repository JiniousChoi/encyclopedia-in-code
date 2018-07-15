package com.paulbutcher

import akka.actor._
import akka.actor.SupervisorStrategy._
import java.util.NoSuchElementException

// START:master
case class Result(result: Any)

class Master extends Actor {

  val cache = context.actorOf(Props[BuggyCache], "cache")

  def receive = {
    case Put(key, value) => cache ! Put(key, value)
    case Get(key) => cache ! Get(key)
    case ReportSize => cache ! ReportSize
    case Result(result) => println(result)
  }

  // START_HIGHLIGHT
  override val supervisorStrategy = OneForOneStrategy() {
      case _: NoSuchElementException => Resume
      case _: NullPointerException => Restart
      case _ => Escalate
    }
  // END_HIGHLIGHT
}
// END:master