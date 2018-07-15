package com.paulbutcher

import akka.actor._

// START:parser
case object Processed

class Parser(counter: ActorRef) extends Actor { //<label id="code.constructor"/>

  val pages = Pages(100000, "enwiki.xml")

  override def preStart {
    for (page <- pages.take(10)) //<label id="code.primepump"/>
      counter ! page
  }

  def receive = {
    case Processed if pages.hasNext => counter ! pages.next //<label id="code.nextpage"/>
    case _ => context.stop(self) //<label id="code.stopself"/>
  }
}
// END:parser