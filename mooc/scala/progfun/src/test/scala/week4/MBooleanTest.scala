package week4

import org.scalatest.FunSuite

class MBooleanTest extends FunSuite {

  test("Martin's Implementation") {
    assert (MTrue === MTrue)
    assert (MFalse === MFalse)
    assert (MTrue !== MFalse)

    assert (!MTrue === MFalse)
    assert (!MFalse === MTrue)

    assert ((MTrue == MTrue) === MTrue)
    assert ((MTrue == MFalse) === MFalse)
    assert ((MFalse == MTrue) === MFalse)
    assert ((MFalse == MFalse) === MTrue)

    assert ((MTrue != MTrue) === MFalse)
    assert ((MTrue != MFalse) === MTrue)
    assert ((MFalse != MTrue) === MTrue)
    assert ((MFalse != MFalse) === MFalse)

    assert ((MTrue && MTrue) === MTrue)
    assert ((MTrue && MFalse) === MFalse)
    assert ((MFalse && MTrue) === MFalse)
    assert ((MFalse && MFalse) === MFalse)

    assert ((MTrue || MTrue) === MTrue)
    assert ((MTrue || MFalse) === MTrue)
    assert ((MFalse || MTrue) === MTrue)
    assert ((MFalse || MFalse) === MFalse)

    assert ((MTrue < MTrue) === MFalse)
    assert ((MTrue < MFalse) === MFalse)
    assert ((MFalse < MTrue) === MTrue)
    assert ((MFalse < MFalse) === MFalse)
  }
}
