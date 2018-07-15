package com.paulbutcher

import akka.actor._

case object Processed

// START:parser
class Parser(counters: ActorRef) extends Actor {

  val pages = Pages(100000, "enwiki.xml")

  override def preStart {
    for (page <- pages.take(100))
      counters ! page
  }

  def receive = {
    case Processed if pages.hasNext => counters ! pages.next
    case _ => context.stop(self)
  }
}
// END:parser