package com.paulbutcher

import akka.actor._
import collection.mutable.{LinkedHashMap, Queue}

// START:parser
case object RequestBatch
case class Processed(id: Int)

class Parser(filename: String, batchSize: Int, limit: Int) extends Actor {

  val pages = Pages(limit, filename)
  var nextId = 1
  val pending = LinkedHashMap[Int, Batch]() //<label id="code.pendingwork"/>

  val accumulator = context.actorOf(Props(new Accumulator(self))) //<label id="code.accumulator"/>

  def receive = {
    case RequestBatch =>
      if (pages.hasNext) {
        val batch = Batch(nextId, pages.take(batchSize).toVector, accumulator) //<label id="code.unparsed"/>
        pending(nextId) = batch
        sender ! batch
        nextId += 1
      } else {
        val (id, batch) = pending.head  // The oldest pending item // <label id="code.pending"/>
        pending -= id                   // Remove and re-add so it's now
        pending(id) = batch             // the youngest
        sender ! batch
      }

    case Processed(id) =>
      pending.remove(id)
      if (!pages.hasNext && pending.isEmpty)
        context.system.shutdown
  }
}
// END:parser