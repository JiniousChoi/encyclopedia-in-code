package week4

abstract class Nat {
  def isZero: Boolean
  def predecessor: Nat
  lazy val successor: Nat = new Succ(this) // Now, every Nat instances including `object Zero` are singletons.
  def + (that: Nat): Nat
  def - (that: Nat): Nat
}

object Zero extends Nat {
  override def isZero: Boolean = true
  override def predecessor: Nat = throw new Error("0.predecessor")
  override def +(that: Nat): Nat = that
  override def -(that: Nat): Nat = if (that isZero) this else throw new Error("negative num")
}

class Succ (val predecessor: Nat) extends Nat {
  override def isZero: Boolean = false
  override def +(that: Nat): Nat = (this predecessor) + (that successor)
  override def -(that: Nat): Nat = if (that isZero) this else this.predecessor - that.predecessor

}
