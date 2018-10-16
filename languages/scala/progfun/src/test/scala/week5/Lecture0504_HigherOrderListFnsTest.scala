package week5

import org.scalatest.FunSuite

class Lecture0504_HigherOrderListFnsTest extends FunSuite{
  val xs1 = List(-3,-2,0,1,2,3)
  val xs1sq = List(9,4,0,1,4,9)
  val xs1pos = List(1,2,3)

  test("squareList") {
    assert (Lecture0504_HigherOrderListFns.Mapping.squareListByPatternMatching(xs1) === xs1sq)
    assert (Lecture0504_HigherOrderListFns.Mapping.squareListByMap(xs1) === xs1sq)
  }

  test("posElems") {
    assert (Lecture0504_HigherOrderListFns.Filtering.posElemsByPatternMatching(xs1) === xs1pos)
    assert (Lecture0504_HigherOrderListFns.Filtering.posElemsByFilter(xs1) === xs1pos)
  }

  test("more higher order methods on list - filter, filterNot, partition") {
    val ys = List(1,2,-3,-4,5,6,-7,-8)
    val ysPos = List(1,2,5,6)
    val ysNotPos = List(-3,-4,-7,-8)
    assert (ys.filter(_>0) === ysPos)
    assert (ys.filterNot(_>0) === ysNotPos)
    assert (ys.partition(_>0) === (ysPos, ysNotPos))
  }

  test("more higher order methods on list - takeWhile, dropWhile, span") {
    val ys = List(1,2,-3,-4,5,6,-7,-8)
    val ysTakenWhile = List(1,2)
    val ysDroppedWhile = List(-3,-4,5,6,-7,-8)
    assert (ys.takeWhile(_>0) === ysTakenWhile)
    assert (ys.dropWhile(_>0) === ysDroppedWhile)
    assert (ys.span(_>0) === (ysTakenWhile, ysDroppedWhile))
  }

  test("pack") {
    val xs = List("a", "a", "a", "b", "c", "c", "a")
    val xsPacked = List(List("a", "a", "a"), List("b"), List("c", "c"), List("a"))
    assert (Lecture0504_HigherOrderListFns.exercise.pack(xs) === xsPacked)
  }

  test("encode") {
    val input = List("a", "a", "a", "b", "c", "c", "a")
    val expected = List(("a", 3), ("b", 1), ("c", 2), ("a", 1))
    assert (Lecture0504_HigherOrderListFns.exercise.encodeByJin(input) === expected)
    assert (Lecture0504_HigherOrderListFns.exercise.encodeByMartin(input) === expected)
  }
}
