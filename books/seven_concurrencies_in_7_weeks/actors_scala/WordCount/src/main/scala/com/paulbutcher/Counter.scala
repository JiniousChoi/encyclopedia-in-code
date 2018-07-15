package com.paulbutcher

import akka.actor._
import collection.mutable.HashMap

// START:counter
class Counter extends Actor {

  val counts = HashMap[String, Int]().withDefaultValue(0)

  // START:receive
  def receive = {
    case Page(title, text) =>
      for (word <- Words(text))
        counts(word) += 1
      // START_HIGHLIGHT
      sender ! Processed
      // END_HIGHLIGHT
  }
  // END:receive
}
// END:counter
