package com.paulbutcher

import akka.actor._
import akka.cluster.ClusterEvent._

// START:testactor
case class HelloFrom(actor: ActorRef)

class TestActor extends Actor {

  def receive = {
    case MemberUp(member) =>
      println(s"Member is up: $member")
      val remotePath = RootActorPath(member.address) / "user" / "test-actor"
      val remote = context.actorFor(remotePath)
      remote ! HelloFrom(self)
      context.watch(remote)

    case HelloFrom(actor) => println(s"Hello from: $actor")
    case Terminated(actor) => println(s"Terminated: $actor")
    case event => println(s"Event: $event")
  }
}
// END:testactor