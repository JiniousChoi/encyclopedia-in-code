package com.paulbutcher

import akka.actor._
import collection.mutable.HashMap

// START:counter
// START_HIGHLIGHT
class Counter(accumulator: ActorRef) extends Actor {
// END_HIGHLIGHT

  val counts = HashMap[String, Int]().withDefaultValue(0)

  def receive = {
    case Page(title, text) =>
      for (word <- Words(text))
        counts(word) += 1
      sender ! Processed
  }

  // START_HIGHLIGHT
  override def postStop() {
    accumulator ! Counts(counts)
  }
  // END_HIGHLIGHT
}
// END:counter