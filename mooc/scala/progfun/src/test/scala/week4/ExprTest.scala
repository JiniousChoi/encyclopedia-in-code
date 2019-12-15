package week4

import org.scalatest.FunSuite

class ExprTest extends FunSuite {

  test("testShow") {
    assert ( (Sum4(Number4(1), Number4(2)) show) === "1 + 2" )
  }

}
