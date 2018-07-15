package com.paulbutcher

import akka.actor._
import collection.Map
import collection.mutable.{HashMap, Set}

// START:accumulator
case class Counts(id: Int, counts: Map[String, Int])

class Accumulator(parser: ActorRef) extends Actor {
  
  val counts = HashMap[String, Int]().withDefaultValue(0)
  val processedIds = Set[Int]()

  def receive = {
    case Counts(id, partialCounts) =>
      if (!processedIds.contains(id)) {
        for ((word, count) <- partialCounts)
          counts(word) += count
        processedIds += id
        parser ! Processed(id)
      }
  }
}
// END:accumulator