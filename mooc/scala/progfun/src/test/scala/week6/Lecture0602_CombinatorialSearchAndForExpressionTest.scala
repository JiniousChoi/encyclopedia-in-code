package week6

import org.scalatest.FunSuite

class Lecture0602_CombinatorialSearchAndForExpressionTest extends FunSuite {
  test("primePairs: imperative") {
    assert (Lecture0602_CombinatorialSearchAndForExpression.primePairs.primePairsImperative(7) ===
            Array((2,1), (3,2), (4,1), (4,3), (5,2), (6,1), (6,5)))
  }

  test("primePairs: higher-order function 1") {
    assert (Lecture0602_CombinatorialSearchAndForExpression.primePairs.primePairsWithHigherOrderFunctions1(7) ===
            List((2,1), (3,2), (4,1), (4,3), (5,2), (6,1), (6,5)))
  }

  test("primePairs: higher-order function 2") {
    assert (Lecture0602_CombinatorialSearchAndForExpression.primePairs.primePairsWithHigherOrderFunctions2(7) ===
      List((2,1), (3,2), (4,1), (4,3), (5,2), (6,1), (6,5)))
  }

  test("primePairs: for-expression") {
    assert (Lecture0602_CombinatorialSearchAndForExpression.primePairs.primePairsWithForExpression(7) ===
            List((2,1), (3,2), (4,1), (4,3), (5,2), (6,1), (6,5)))
  }

  test("exercise: scalarProduct") {
    val xs = List(1,2,3)
    val ys = List(3,2,1)
    val expected = 10
    assert (Lecture0602_CombinatorialSearchAndForExpression.exercise.scalarProduct(xs, ys) === expected)
  }
}
