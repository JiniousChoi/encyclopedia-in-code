package week5

import org.scalatest.FunSuite

class Lecture0503_ImplicitParametersTest extends FunSuite {
  val ints_unsorted = List(3,2,1)
  val ints_sorted = List(1,2,3)
  val fruits_unsorted = List("apple", "pineapple", "orange", "banana")
  val fruits_sorted = List("apple", "banana", "orange", "pineapple")

  test("[lt] explicit") {
    assert (Lecture0503_ImplicitParameters.LT.msort(ints_unsorted)((x: Int, y: Int) => x < y) === ints_sorted)
    assert (Lecture0503_ImplicitParameters.LT.msort(fruits_unsorted)((x:String, y:String) => x.compareTo(y) < 0) === fruits_sorted)
  }

  test("[lt] inferred") {
    /* That discussion shows that it's usually advantageous if you have several parameter lists and
    *  one of them is a function value, to put the function value last. Because then you have
    *  a better chance that the type's already inferred by the time the compiler will type check
    *  the function value and that means you don't have to write them explicitly. */
    assert (Lecture0503_ImplicitParameters.LT.msort(ints_unsorted)((x, y) => x < y) === ints_sorted)
    assert (Lecture0503_ImplicitParameters.LT.msort(fruits_unsorted)((x, y) => x.compareTo(y) < 0) === fruits_sorted)
  }

  test("[ord] explicit") {
    assert (Lecture0503_ImplicitParameters.ORD.msort(ints_unsorted)(Ordering.Int) === ints_sorted)
    assert (Lecture0503_ImplicitParameters.ORD.msort(fruits_unsorted)(Ordering.String) === fruits_sorted)
  }

  test("[ord] implicity") {
    /* Now it's just as concise and nice as in the case of Lecture0502_PairsAndTuples.msort
    * but it's even fully parametric */
    assert (Lecture0503_ImplicitParameters.ORD_IMPLICIT.msort(ints_unsorted) === ints_sorted)
    assert (Lecture0503_ImplicitParameters.ORD_IMPLICIT.msort(fruits_unsorted) === fruits_sorted)
  }
}
