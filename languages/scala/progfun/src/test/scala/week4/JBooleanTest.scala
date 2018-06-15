package week4

import org.scalatest.FunSuite

class JBooleanTest extends FunSuite {

  test("My Implementation") {
    assert (JTrue === JTrue)
    assert (JFalse === JFalse)
    assert (JTrue !== JFalse)

    assert (!JTrue === JFalse)
    assert (!JFalse === JTrue)

    assert ((JTrue == JTrue) === JTrue)
    assert ((JTrue == JFalse) === JFalse)
    assert ((JFalse == JTrue) === JFalse)
    assert ((JFalse == JFalse) === JTrue)

    assert ((JTrue != JTrue) === JFalse)
    assert ((JTrue != JFalse) === JTrue)
    assert ((JFalse != JTrue) === JTrue)
    assert ((JFalse != JFalse) === JFalse)

    assert ((JTrue && JTrue) === JTrue)
    assert ((JTrue && JFalse) === JFalse)
    assert ((JFalse && JTrue) === JFalse)
    assert ((JFalse && JFalse) === JFalse)

    assert ((JTrue || JTrue) === JTrue)
    assert ((JTrue || JFalse) === JTrue)
    assert ((JFalse || JTrue) === JTrue)
    assert ((JFalse || JFalse) === JFalse)

    assert ((JTrue < JTrue) === JFalse)
    assert ((JTrue < JFalse) === JFalse)
    assert ((JFalse < JTrue) === JTrue)
    assert ((JFalse < JFalse) === JFalse)
  }
}
