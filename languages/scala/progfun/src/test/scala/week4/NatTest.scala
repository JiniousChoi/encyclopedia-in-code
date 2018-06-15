package week4

import org.scalatest.FunSuite

class NatTest extends FunSuite {

  trait TestBde {
    def calcNum(nat: Nat): Int = {
      if (nat.isZero) 0
      else 1 + calcNum(nat.predecessor)
    }

    val zero = Zero
    val one = zero.successor
    val two = one.successor
    val three = two.successor
  }

  test("Instantiation") {
    new TestBde {
      assert(calcNum(zero) === 0)
      assert(calcNum(one) === 1)
      assert(calcNum(two) === 2)

    }
  }

  test("Arithmetic Operation") {
    new TestBde {
      assert (zero == two-two)
      assert (calcNum(two + three) == 5)
      assert (calcNum(three - two) == 1)

      assert (zero.successor == zero.successor)
    }
  }

  test("Object Equity") {
   new TestBde {
      assert (zero.successor == zero.successor)
     assert (zero.successor.successor.predecessor.predecessor == zero)
    }
  }
}
