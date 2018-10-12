package week5

/*
 * We will discuss more higher-order functions such as fold, and reduce combinators.
 * There's several variance of these combinators, but what they have in common is that
 * they insert and give an operator between adjacent elements of a list.
 */

object Lesson0505_ReductionOfLists {
  object Sum {
    def byReduceLeft (xs: List[Int]): Int =
      (0 :: xs) reduceLeft (_ + _)

    def byFoldLeft (xs: List[Int]): Int =
      xs.foldLeft(0)(_ + _)
  }

  object Times {
    def byReduceLeft (xs: List[Int]): Int =
      (1 :: xs) reduceLeft (_ * _)

    def byFoldLeft (xs: List[Int]): Int =
      xs.foldLeft(1)(_ * _)
  }

  object Impl {
    // reduce methods are different from fold methods type-wise
    def reduceLeft[T] (xs: List[T])(op: (T,T) => T): T = xs match {
      case Nil => throw new Error("Nil.reduceLeft")
      case x::xs1 => foldLeft(xs1)(x)(op)
    }
    // fold methods are morre flexible & generic compared to reduce methods
    // because the acc would be kept out of xs being independent of the type xs elements,
    // whilst the reduce methods need to keep acc inside xs.
    def foldLeft[T,U] (xs: List[T])(acc: U)(op: (U,T) => U): U = xs match {
      case Nil => acc
      case x::xs1 => foldLeft(xs1)(op(acc,x))(op)
    }

  }
}
