package week3

trait List[T] {
  def head: T
  def tail: List[T]
  def isEmpty: Boolean
}

class Nil[T] extends List[T] {
  def head: Nothing = throw new NoSuchElementException("Nil.head")
  def tail: Nothing = throw new NoSuchElementException("Nil.tail")
  def isEmpty: Boolean = true
}

class Cons[T](val head: T, val tail: List[T]) extends List[T] {
  def isEmpty: Boolean = false
}

