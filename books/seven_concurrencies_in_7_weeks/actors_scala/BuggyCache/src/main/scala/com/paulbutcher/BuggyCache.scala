package com.paulbutcher

import akka.actor._
import collection.mutable.HashMap

// START:cache
case class Put(key: String, value: String)
case class Get(key: String)
case object ReportSize

class BuggyCache extends Actor {

  val cache = HashMap[String, String]()
  var size = 0

  def receive = {
    case Put(key, value) =>
      cache(key) = value
      size += value.length

    case Get(key) => sender ! Result(cache(key))

    case ReportSize => sender ! Result(size)
  }

  override def postRestart(reason: Throwable) {
    println("BuggyCache has restarted")
  }
}
// END:cache