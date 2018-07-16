package aia.testdriven

import akka.testkit.{ CallingThreadDispatcher, EventFilter, TestKit }
import akka.actor.{ Props, ActorSystem }
import com.typesafe.config.ConfigFactory
import org.scalatest.WordSpecLike

// because of
// 1. to use the Greeter01Test object which is defined later than Greeter01Test class
// 2. to use Greeter Actor in /src/main/scala/aia/testdriven
import Greeter01Test._

class Greeter01Test extends TestKit(testSystem)
  with WordSpecLike
  with StopSystemAfterAll {

  "The Greeter" must {
    "say Hello World! when a Greeting(\"World\") is sent to it" in {
      val dispatcherId = CallingThreadDispatcher.Id
      val props = Props[Greeter].withDispatcher(dispatcherId)
      val greeter = system.actorOf(props)
      EventFilter.info(message = "Hello World!",
        occurrences = 1).intercept {
          greeter ! Greeting("World")
        }
    }
  }
}

object Greeter01Test {
  val testSystem = {
    val config = ConfigFactory.parseString(
      """
         akka.loggers = [akka.testkit.TestEventListener]
      """)
    ActorSystem("testsystem", config)
  }
}

