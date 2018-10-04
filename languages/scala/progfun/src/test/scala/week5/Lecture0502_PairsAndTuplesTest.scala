package week5

import org.scalatest.FunSuite

class Lecture0502_PairsAndTuplesTest extends FunSuite {
  val xs0 = List()
  val xs1 = List(1)
  val xs2_1 = List(1,2)
  val xs2_2 = List(2,1)
  val xs3_1 = List(1,2,3)
  val xs3_2 = List(1,3,2)
  val xs3_3 = List(2,1,3)
  val xs3_4 = List(2,3,1)
  val xs3_5 = List(3,1,2)
  val xs3_6 = List(3,2,1)

  test("zero_and_one") {
    assert (Lecture0502_PairsAndTuples.msort(xs0) === xs0)
    assert (Lecture0502_PairsAndTuples.msort(xs1) === xs1)
  }

  test("twos") {
    assert (Lecture0502_PairsAndTuples.msort(xs2_1) === List(1,2))
    assert (Lecture0502_PairsAndTuples.msort(xs2_2) === List(1,2))
  }

  test("threes") {
    val expected = List(1,2,3)
    assert (Lecture0502_PairsAndTuples.msort(xs3_1) === expected)
    assert (Lecture0502_PairsAndTuples.msort(xs3_2) === expected)
    assert (Lecture0502_PairsAndTuples.msort(xs3_3) === expected)
    assert (Lecture0502_PairsAndTuples.msort(xs3_4) === expected)
    assert (Lecture0502_PairsAndTuples.msort(xs3_5) === expected)
    assert (Lecture0502_PairsAndTuples.msort(xs3_6) === expected)
  }
}
