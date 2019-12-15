import scala.annotation.tailrec
import scala.collection.immutable.List

def isort1(xs: List[Int]): List[Int] = {
  // By Martin
  def insert(x: Int, ys: List[Int]): List[Int] = ys match {
    case Nil => x::Nil
    case y::ys1 => if (x <= y) x::ys else y::insert(x, ys1)
  }
  xs match {
    case Nil => Nil
    case y::ys => insert(y, isort1(ys))
  }
}

def isort2(xs: List[Int]): List[Int] = {
  // By Jin
  def insert(x: Int, acc: List[Int]): List[Int] = acc match {
    case Nil  => x :: Nil
    case y::ys =>
      if (x <= y) x :: acc
      else y :: insert(x, ys)
  }

  @tailrec
  def loop(acc: List[Int], xs: List[Int]): List[Int] = xs match {
    case Nil => acc
    case y::ys => loop(insert(y, acc), ys)
  }

  loop(Nil, xs)
}

def hsort(xs: List[Int]): List[Int] = ???

def qsort(xs: List[Int]): List[Int] = xs match {
  case Nil => xs
  case y::ys => {
    val (l,r) = ys partition(_ <= y)
    qsort(l) ++ (y :: qsort(r))
  }
}

def msort(xs: List[Int]): List[Int] = {
  def merge(xs: List[Int], ys: List[Int]): List[Int] = (xs, ys) match {
    case (_, Nil) => xs
    case (Nil, _) => ys
    case (x :: xs1, y :: ys1) =>
      if (x <= y) x :: merge(xs1, ys)
      else y :: merge(xs, ys1)
  }

  xs match {
    case Nil => xs
    case x :: Nil => xs
    case _ => {
      val (l, r) = xs splitAt (xs.length / 2)
      val (l2, r2) = (msort(l), msort(r))
      merge(l2, r2)
    }
  }
}

println("qsort test")
val xs = List(3,1,5,4,2,1)
println(qsort(xs))

println("msort test")
println(msort(xs))

println("isort1 test")
println(isort1(xs))

println("isort2 test")
println(isort2(xs))