package week6

import org.scalatest.FunSuite

class Lecture0601_OtherCollectionsTest extends FunSuite {
  test("Vector") {
    val v1 = Vector(2)
    val v2 = 1 +: v1
    val v3 = v2 :+ 3
    assert (v3 == Vector(1,2,3))
    assert (v3.map(_*3) == Vector(3,6,9))
    assert (v3.filter(_>1) == Vector(2,3))

    assert (this.head(v3) == 1)
  }

  def head[T](vec: Vector[T]): T = vec match {
    case Vector() => throw new Error("Vector().head")
    case x+:xs1 => x
  }

  test("Array") {
    val xs = Array(1, 2, 3, 44)
    assert ( (xs map (x => x * 2)) === Array(2, 4, 6, 88))
    assert ( (xs filter (x => x > 20)) === Array(44))
  }

  test("String") {
    val s = "Hello World"
    assert ((s filter (c => c.isUpper)) == "HW")
  }

  test("Range") {
    // Another simple kind of sequence
    val xs = (1 to 5) map (_+1)
    assert (xs == (2 to 6))
    assert (xs == List(2,3,4,5,6))

    val ys = (2 to 1)
    assert (ys == List())
  }

  test("some more sequence operations") {
    val xs = List(1,2,3)
    val ys = "Hello Jin"
    val mns = List((1,2), (2,4), (3,6))
    assert (xs.forall(_>0))
    assert (xs.exists(_==2))
    assert (xs.max == 3)
    assert (xs.min == 1)
    assert (xs.product == 6)
    assert (xs.sum == 6)

    assert (xs.zip(ys) === List((1,'H'), (2, 'e'), (3, 'l')))

    assert (mns.unzip === (List(1,2,3), List(2,4,6)))
  }

  test("exercise: combination") {
    val actual = Lecture0601_OtherCollections.exercise.combi(3,2)
    val expected = List((1,1), (1,2), (2,1), (2,2), (3,1), (3,2))
    assert (actual == expected)
  }

  test("exercise: scalarProduct") {
    val xs = Vector(1,2,3)
    val ys = Vector(3,2,1)
    val actual1 = Lecture0601_OtherCollections.exercise.scalarProduct(xs, ys)
    val actual2 = Lecture0601_OtherCollections.exercise.scalarProductWithPatternMatching(xs, ys)
    val expected = 3+4+3
    assert (actual1 == expected)
    assert (actual2 == expected)
  }

  test("exercise: isPrime") {
    assert (Lecture0601_OtherCollections.exercise.isPrime(2))
    assert (Lecture0601_OtherCollections.exercise.isPrime(3))
    assert (Lecture0601_OtherCollections.exercise.isPrime(5))
    assert (Lecture0601_OtherCollections.exercise.isPrime(7))

    assert (! Lecture0601_OtherCollections.exercise.isPrime(1))
    assert (! Lecture0601_OtherCollections.exercise.isPrime(4))
    assert (! Lecture0601_OtherCollections.exercise.isPrime(6))
    assert (! Lecture0601_OtherCollections.exercise.isPrime(8))
    assert (! Lecture0601_OtherCollections.exercise.isPrime(9))
    assert (! Lecture0601_OtherCollections.exercise.isPrime(10))
  }
}
