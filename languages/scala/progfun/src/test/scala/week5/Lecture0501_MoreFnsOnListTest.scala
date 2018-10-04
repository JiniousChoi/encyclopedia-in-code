package week5

import org.scalatest.FunSuite

class Lecture0501_MoreFnsOnListTest extends FunSuite {
  val xs = List(1,2,3)
  val ys = List(4,5,6)

  test("last") {
    assert (Lecture0501_MoreFnsOnList.last(xs) === 3)
  }

  test("init") {
    assert (Lecture0501_MoreFnsOnList.init(xs) === List(1,2))
  }

  test("concat") {
    assert (Lecture0501_MoreFnsOnList.concat(xs, ys) === List(1,2,3,4,5,6))
  }

  test("reverse") {
    assert (Lecture0501_MoreFnsOnList.reverse(xs) === List(3,2,1))
  }

  test("removeAtByJin") {
    assert (Lecture0501_MoreFnsOnList.removeAtByJin(-1, xs) === xs)
    assert (Lecture0501_MoreFnsOnList.removeAtByJin(0, xs) === List(2,3))
    assert (Lecture0501_MoreFnsOnList.removeAtByJin(1, xs) === List(1,3))
    assert (Lecture0501_MoreFnsOnList.removeAtByJin(2, xs) === List(1,2))
    assert (Lecture0501_MoreFnsOnList.removeAtByJin(3, xs) === xs)
  }

  test("removeAtByMartin") {
    assert (Lecture0501_MoreFnsOnList.removeAtByMartin(-1, xs) === xs)
    assert (Lecture0501_MoreFnsOnList.removeAtByMartin(0, xs) === List(2,3))
    assert (Lecture0501_MoreFnsOnList.removeAtByMartin(1, xs) === List(1,3))
    assert (Lecture0501_MoreFnsOnList.removeAtByMartin(2, xs) === List(1,2))
    assert (Lecture0501_MoreFnsOnList.removeAtByMartin(3, xs) === xs)
  }
}
