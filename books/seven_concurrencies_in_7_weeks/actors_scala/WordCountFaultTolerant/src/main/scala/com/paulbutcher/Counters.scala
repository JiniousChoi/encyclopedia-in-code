package com.paulbutcher

import akka.actor._
import akka.cluster._
import ClusterEvent._
import MemberStatus._
import akka.routing.BroadcastRouter

// START:counters
class Counters(count: Int) extends Actor {

  val counters = context.actorOf(Props[Counter].
    withRouter(new BroadcastRouter(count)), "counter")

  override def preStart {
    Cluster(context.system).subscribe(self, classOf[MemberUp])
  }

  def receive = {
    case state: CurrentClusterState =>
      for (member <- state.members if (member.status == Up))
        counters ! ParserAvailable(findParser(member))

    case MemberUp(member) => counters ! ParserAvailable(findParser(member))
  }

  def findParser(member: Member) = 
    context.actorFor(RootActorPath(member.address) / "user" / "parser")
}
// END:counters