package week4

//useless since type may only be Nothing
trait InvariantList1[T] {
  def isEmpty: Boolean
  def head: T
  def tail: InvariantList1[T]
}
object InvariantNil1 extends InvariantList1[Nothing] {
  override def isEmpty: Boolean = true
  override def head: Nothing = throw new Error("empty.head")
  override def tail: InvariantList1[Nothing] = throw new Error("empty.tail")
}
class InvariantCons1[T](val head:T, val tail: InvariantList1[T]) extends InvariantList1[T] {
  override def isEmpty: Boolean = false
}

// list of homogeneous typee. InvariantNil2 can never be singleton object.
trait InvariantList2[T] {
  def isEmpty: Boolean
  def head: T
  def tail: InvariantList2[T]
}
class InvariantNil2[T] extends InvariantList2[T] {
  override def isEmpty: Boolean = true
  override def head: T = throw new Error("empty.head")
  override def tail: InvariantList2[T] = throw new Error("empty.tail")
}
class InvariantCons2[T](val head:T, val tail: InvariantList2[T]) extends InvariantList2[T] {
  override def isEmpty: Boolean = false
}

// From here it's all about list of heterogeneous type

// Although this list is of heterogeneous type, it's uncomfortable to use create new Cons instance using constructor.
// a covariant method that prepend to a list would be great.
trait CovariantList1[+T] {
  def isEmpty: Boolean
  def head: T
  def tail: CovariantList1[T]
}
object CovariantNil1 extends CovariantList1[Nothing] {
  override def isEmpty: Boolean = true
  override def head: Nothing = throw new Error("empty.head")
  override def tail: CovariantList1[Nothing] = throw new Error("empty.tail")
}
class CovariantCons1[T](val head:T, val tail: CovariantList1[T]) extends CovariantList1[T] {
  override def isEmpty: Boolean = false
}

// Nice to introduce `prepend` method! But, how aboult extracting the duplicated in subclasses into the trait?
// See CovariantList3
trait CovariantList2[+T] {
  def isEmpty: Boolean
  def head: T
  def tail: CovariantList2[T]
  def prepend[U >: T](elem: U): CovariantList2[U] // abstract method
}
object CovariantNil2 extends CovariantList2[Nothing] {
  override def isEmpty: Boolean = true
  override def head: Nothing = throw new Error("empty.head")
  override def tail: CovariantList2[Nothing] = throw new Error("empty.tail")
  def prepend[U >: Nothing](elem: U) : CovariantList2[U] = new CovariantCons2(elem, this) // implement abstract method; because T is Nothing in this Nil object
}
class CovariantCons2[T](val head:T, val tail: CovariantList2[T]) extends CovariantList2[T] {
  override def isEmpty: Boolean = false
  override def prepend[U >: T](elem: U) : CovariantList2[U] = new CovariantCons2(elem, this) // implement abstract method
}

// final version
trait CovariantList3[+T] {
  def isEmpty: Boolean
  def head: T
  def tail: CovariantList3[T]
  def prepend[U >: T](elem: U) : CovariantList3[U] = new CovariantCons3(elem, this)
}
object CovariantNil3 extends CovariantList3[Nothing] {
  override def isEmpty: Boolean = true
  override def head: Nothing = throw new Error("empty.head")
  override def tail: CovariantList3[Nothing] = throw new Error("empty.tail")
}
class CovariantCons3[T](val head:T, val tail: CovariantList3[T]) extends CovariantList3[T] {
  override def isEmpty: Boolean = false
}
