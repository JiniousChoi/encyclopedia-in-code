package week6

import Lecture0601_OtherCollections.exercise.isPrime

object Lecture0602_CombinatorialSearchAndForExpression {

  object primePairs {

    def primePairsImperative(n: Int) = {
      val arrayBuffer = scala.collection.mutable.ArrayBuffer.empty[(Int, Int)]
      for (a <- 1 until n) {
        for (b <- 1 until a) {
          if (isPrime(a + b)) {
            arrayBuffer += ((a, b))
          }
        }
      }
      arrayBuffer.toArray
    }

    def primePairsWithHigherOrderFunctions1(n: Int) = {
      (1 until n) flatMap (a =>
        (1 until a) map (b =>
          (a,b)
        )
      ) filter (pair => isPrime(pair._1 + pair._2))
    }

    def primePairsWithHigherOrderFunctions2(n: Int) = {
      val pairs = (1 until n) map (a => (1 until a) map (b => (a,b) ) )
      pairs.flatten filter {case (a,b) => isPrime(a + b)}
    }

    def primePairsWithForExpression(n: Int) =
      for {
        a <- 1 until n
        b <- 1 until a
        if isPrime(a+b)
      } yield (a,b)
  }

  object exercise {
    def scalarProduct(xs: List[Int], ys: List[Int]) = {
      (for ((x,y) <- xs zip ys) yield x*y) sum
    }
  }
}
