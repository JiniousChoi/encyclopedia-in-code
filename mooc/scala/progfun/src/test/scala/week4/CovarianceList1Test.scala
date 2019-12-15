package week4

import org.scalatest.FunSuite

class CovarianceList1Test extends FunSuite {

  class Animal
  class Human extends Animal
  class Dog extends Animal

  test("InvariantList1 is useless.") {
    val empty = InvariantNil1
    // Compile Error Expected
    // uncomment and then run it to see the following error message
    // BTW, by just uncommenting it doesn't show grammar error check in IntellJ. Maybe it's not yet implemented?
    // Shouldn't it show some error in red if it's going to fail in complile time, eventually, someday?
    //new InvariantCons(new Animal(), empty)
    /**
      * Error:(14, 37) type mismatch;
      * found   : week4.InvariantNil.type
      * required: week4.InvariantList[week4.Animal]
      * Note: Nothing <: week4.Animal (and week4.InvariantNil.type <: week4.InvariantList[Nothing]), but trait InvariantList is invariant in type T.
      * You may wish to define T as +T instead. (SLS 4.5)
      * new InvariantCons(new Animal(), empty) // Compile Error Expected
      */
  }

  test("InvariantList2 is homogeneous") {
    val empty = new InvariantNil2[Dog];
    val ls1: InvariantList2[Dog] = new InvariantCons2[Dog](new Dog(), empty);
    val ls2: InvariantList2[Dog] = new InvariantCons2[Dog](new Dog(), ls1);
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
    val empty: CovariantList3[Nothing] = CovariantNil3
    val ls1: CovariantList3[Human] = empty.prepend(new Human())
    val ls2: CovariantList3[Animal] = ls1.prepend(new Dog())
  }
}
