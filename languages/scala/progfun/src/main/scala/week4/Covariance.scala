package week4

trait InvariantList[T] {
  def isEmpty: Boolean
  def head: T
  def tail: InvariantList[T]
}

object InvariantNil extends InvariantList[Nothing] {
  override def isEmpty: Boolean = true
  override def head: Nothing = throw new Error("empty.head")
  override def tail: InvariantList[Nothing] = throw new Error("empty.tail")
}

class InvariantCons[T](val head:T, val tail: InvariantList[T]) extends InvariantList[T] {
  override def isEmpty: Boolean = false
}


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


trait CovariantList2[+T] {
  def isEmpty: Boolean
  def head: T
  def tail: CovariantList2[T]
  //def prepend(elem: T) : CovariantList2[T] = new CovariantCons2(elem, this) // Error
  //def prepend[U >: T](elemn: U): CovariantList2[U] // abstract method
  def prepend[U >: T](elem: U) : CovariantList2[U] = new CovariantCons2(elem, this)
}

object CovariantNil2 extends CovariantList2[Nothing] {
  override def isEmpty: Boolean = true
  override def head: Nothing = throw new Error("empty.head")
  override def tail: CovariantList2[Nothing] = throw new Error("empty.tail")
  //def prepend[U >: Nothing](elem: U) : CovariantList2[U] = new CovariantCons2(elem, this) // implement abstract method; because T is Nothing in this Nil object
}

class CovariantCons2[T](val head:T, val tail: CovariantList2[T]) extends CovariantList2[T] {
  override def isEmpty: Boolean = false
  //override def prepend[U >: T](elem: U) : CovariantList2[U] = new CovariantCons2(elem, this) // implement abstract method
}

