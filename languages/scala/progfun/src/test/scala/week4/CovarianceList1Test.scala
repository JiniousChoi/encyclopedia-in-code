package week4

import org.scalatest.FunSuite

class Animal
class Human extends Animal
class Dog extends Animal

class CovarianceList1Test extends FunSuite {

  test("invariant") {
    val empty = InvariantNil
    // Compile Error Expected
    // uncomment and then run it to see the following error message
    // BTW, by just uncommenting it doesn't show grammar error check in IntellJ. Maybe it's not yet implemented?
    // Shouldn't it show some error in red if it's going to fail in complile time, eventually, someday?
    // new InvariantCons(new Animal(), empty)
    /**
      * Error:(14, 37) type mismatch;
      * found   : week4.InvariantNil.type
      * required: week4.InvariantList[week4.Animal]
      * Note: Nothing <: week4.Animal (and week4.InvariantNil.type <: week4.InvariantList[Nothing]), but trait InvariantList is invariant in type T.
      * You may wish to define T as +T instead. (SLS 4.5)
      * new InvariantCons(new Animal(), empty) // Compile Error Expected
      */
  }

  test("Use Covariant Type Parameter to make Nil as an singleton object") {
    val empty: CovariantList1[Nothing] = CovariantNil1
    new CovariantCons1(3, empty)
  }

  test("Using Covariant Type Parameter enables adding any type of instances to it") {
    val empty: CovariantList1[Nothing] = CovariantNil1
    val ls1: CovariantList1[Animal] = new CovariantCons1(new Animal(), empty)
    val ls2: CovariantList1[Animal] = new CovariantCons1(new Human(), ls1)
    val ls3: CovariantList1[Animal] = new CovariantCons1(new Dog(), ls2)
    val ls4: CovariantList1[Any] = new CovariantCons1(3, ls3)
    val ls5: CovariantList1[Any] = new CovariantCons1((1,2), ls4)
  }

  test("prepend needs lower bound type parameter") {
    val empty: CovariantList2[Nothing] = CovariantNil2
    val ls1: CovariantList2[Human] = empty.prepend(new Human())
    val ls2: CovariantList2[Animal] = ls1.prepend(new Dog())
  }
}
