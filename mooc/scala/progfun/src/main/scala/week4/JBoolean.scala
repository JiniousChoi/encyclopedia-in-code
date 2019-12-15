package week4

trait JBoolean {


  def && (that: JBoolean): JBoolean
  def || (that: JBoolean): JBoolean
  def unary_! : JBoolean

  // def == (x: MBoolean): MBoolean = ifThenElse(MTrue, !x) // Impossible to implement without ifThenElse method
  // def != (x: MBoolean): MBoolean = !(this == x) // However, JTrue and JFalse are singleton object, hence ==, != works anyways

  def < (that: JBoolean): JBoolean
}

object JTrue extends JBoolean {
  override def unary_! : JBoolean = JFalse
  override def &&(that: JBoolean): JBoolean = that
  override def ||(that: JBoolean): JBoolean = this
  override def <(that: JBoolean): JBoolean = JFalse
}

object JFalse extends JBoolean {
  override def unary_! : JBoolean = JTrue
  override def &&(that: JBoolean): JBoolean = this
  override def ||(that: JBoolean): JBoolean = that
  override def <(that: JBoolean): JBoolean = that
}
