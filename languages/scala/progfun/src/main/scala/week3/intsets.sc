abstract class IntSet {
  def contains(x: Int): Boolean
  def incl(x: Int): IntSet
  def union(other: IntSet): IntSet
}

object Empty extends IntSet {
  override def contains(x: Int): Boolean = false

  override def incl(x: Int): IntSet =
    new NonEmpty(x, Empty, Empty)

  override def union(other: IntSet): IntSet = other

  override def toString(): String = ""
}

class NonEmpty(elem: Int, left: IntSet = Empty, right: IntSet = Empty) extends IntSet {
  override def contains(x: Int): Boolean =
    if (elem == x) true
    else if (x < elem) left contains x
    else right contains x

  override def incl(x: Int): IntSet =
    if (elem == x) this
    else if (x < elem) new NonEmpty(elem, left incl x, right)
    else new NonEmpty(elem, left, right incl x)

  override def union(other: IntSet): IntSet =
    ((left union right) union other) incl elem

  override def toString(): String =
    "{" + left + " , " + elem + " , " + right + "}"
}

val tree1 = new NonEmpty(3, new NonEmpty(2), new NonEmpty(5))
val tree2 = new NonEmpty(4, new NonEmpty(1), new NonEmpty(8))
tree1 union tree2