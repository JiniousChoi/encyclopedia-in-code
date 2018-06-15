package week4
// Note: This is how an OOP(Polymorphism, to be specific) would eliminate if-else parts
abstract class MBoolean {
  def ifThenElse[T] (t: => T, e: => T): T
  // def ifThenElse(t: => MBoolean, e: => MBoolean): MBoolean
  // Why use generic type here? non-generic seems enough, if not technically the same as the generic one, on terms of post-compilation.

  def && (x: MBoolean): MBoolean = ifThenElse(x, MFalse)
  def || (x: MBoolean): MBoolean = ifThenElse(MTrue, x)
  def unary_! : MBoolean = ifThenElse(MFalse, MTrue)

  def == (x: MBoolean): MBoolean = ifThenElse(x, !x)
  def != (x: MBoolean): MBoolean = !(this == x)

  def < (x: MBoolean): MBoolean = ifThenElse(MFalse, x)
}

object MTrue extends MBoolean {
  override def ifThenElse[T](t: => T, e: => T): T = t
}

object MFalse extends MBoolean {
  override def ifThenElse[T](t: => T, e: => T): T = e
}
