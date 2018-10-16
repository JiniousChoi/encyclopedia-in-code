package week5

import org.scalatest.FunSuite

class Lecture0505_ReductionOfListsTest extends FunSuite {
  test("fold is more flexible than reduce") {
    val fruits = List("apple", "banana", "grape")
    val fruits2 = List("apple", "banana")
    val fruits1 = List("apple")
    assert (fruits.foldLeft("")((acc: String, y: String) => acc + y) === "applebananagrape")
    assert (fruits.foldLeft(0)((acc: Int, y: String) => acc + y.length) === 16)
    assert (fruits.foldLeft(0)((acc: Int, y: String) => acc + 1) === 3)

    assert (fruits.reduceLeft((x: String, y: String) => x + y) === "applebananagrape")

    // assert (fruits.reduceLeft((x: String, y: String) => x.length + y.length) === 16) // Error
    // * One way to understand why the error
    // String-typed list ["apple", "banana", "grape"] becomes Any-typed list [11, "grape"] by the op above
    // now type of `(String, String) => Int` op cannot be applied to [0, "grape"], hence the following error.
    // * Actual reason of the error by the compiler
    // [error]  found   : (String, String) => Int
    // [error]  required: (Any, String) => Any
    // [error]     assert (fruits.reduceLeft((x: String, y: String) => x.length + y.length) === 16)
    // def reduceLeft[B >: A](op: (B, A) => B): B = ???
    // A is String. And the op should conform to `(B>:A, A) => B>:A`.
    // The possible type of op would be like
    // 1. (String, String) => String
    // 2. (Any, String) => Any
    // and so on ...
    // But the type of the given `op`  is `(String, String) => Int
    // Which doesn't conform tot eh possible types of candidate ops
    // THe compiler might have assumed that String and Int need to be get abstracted to their
    // least common ancestor type, which is Any, hence the error:
    // found (String, String) => Int, required: (Any, String) => Any

    // One hacky way to sum of all the given strings in a list with reduceLeft
    assert (("0"::fruits).reduceLeft((x: String, y: String) => (x.toInt + y.length).toString) === "16")
  }

  test("Impl") {
    val xs = List(1,2,3,4,5)
    assert (Lecture0505_ReductionOfLists.Impl.reduceLeft(xs)(_ + _) == 15)
    assert (Lecture0505_ReductionOfLists.Impl.reduceRight(xs)(_ + _) == 15)
    assert (Lecture0505_ReductionOfLists.Impl.foldLeft(xs)(0)(_ + _) == 15)
    assert (Lecture0505_ReductionOfLists.Impl.foldRight(xs)(0)(_ + _) == 15)

    assert (Lecture0505_ReductionOfLists.Impl.foldLeft(xs)("")((acc, x) => acc + x.toString*x) == "122333444455555")
    assert (Lecture0505_ReductionOfLists.Impl.foldRight(xs)("")((x, acc) => x.toString*x + acc) == "122333444455555")
  }

  test("Impl2") {
    val xs = List(1,2,3)
    val ys = List(4,5,6)
    assert (Lecture0505_ReductionOfLists.Impl2.concat(xs, ys) === List(1,2,3,4,5,6))
  }

  test("exercise") {
    val xs = List("jin", "choi", "rocks")
    assert (Lecture0505_ReductionOfLists.exercise.mapFun(xs, (x:String)=>x.size) === List(3,4,5))
    assert (Lecture0505_ReductionOfLists.exercise.lengthFun(xs) === 3)
  }

}
