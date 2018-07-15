package com.paulbutcher

import akka.actor._
import collection.Map
import collection.mutable.HashMap

// START:accumulator
case class Counts(counts: Map[String, Int])

class Accumulator extends Actor {
  
  val counts = HashMap[String, Int]().withDefaultValue(0)

  def receive = {
    case Counts(partialCounts) =>
      for ((word, count) <- partialCounts)
        counts(word) += count
  }
// END:accumulator

  override def postStop() {
    // for ((k, v) <- counts)
    //   println(s"$k=$v")
  }
// START:accumulator
}
// END:accumulator
