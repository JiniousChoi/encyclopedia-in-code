package week5

// # more functions on list
// to study its implementation we might as well define it
// as external functions outside the list class

object Lecture0501_MoreFnsOnList {
  // Time Complexity : O(n)
  def last[T](xs : List[T]) : T = xs match {
    case List() => throw new Error("last of empty list")
    case List(x) => x
    case y::ys => last(ys)
  }

  // Time Complexity : O(n)
  def init[T](xs : List[T]) : List[T] = xs match {
    case List() => throw new Error("init of empty list")
    case List(x) => List()
    case y::ys => y::init(ys)
  }

  // Time Complexity : O(|xs|)
  def concat[T](xs : List[T], ys : List[T]) : List[T] = xs match {
    case List() => ys
    case z::zs => z :: concat(zs, ys)
  }

  // Time Complexity : O(n*n)
  def reverse[T](xs: List[T]) : List[T] = xs match {
    case List() => xs
    case z::zs => reverse(zs) ::: List(z)
  }

  def removeAtByJin[T](n: Int, xs: List[T]) : List[T] = {
    if (0 <= n && n < xs.size) {
      val (ys, zs) = xs.splitAt(n)
      ys ++ zs.tail
    }
    else xs
  }

  def removeAtByMartin[T](n: Int, xs: List[T]) : List[T] = xs.take(n) ::: xs.drop(n+1)
}
