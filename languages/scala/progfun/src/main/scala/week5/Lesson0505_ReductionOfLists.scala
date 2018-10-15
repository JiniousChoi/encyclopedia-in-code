package week5

import scala.annotation.tailrec

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
    @tailrec // resulting in better performance compared to foldRight
    def foldLeft[T,U] (xs: List[T])(acc: U)(op: (U,T) => U): U = xs match {
      case Nil => acc
      case x::xs1 => foldLeft(xs1)(op(acc,x))(op)
    }
    def reduceRight[T] (xs: List[T])(op: (T,T) => T): T = xs match {
      case Nil => throw new Error("Nil.reduceRight")
      case x::xs1 => foldRight(xs1)(x)(op)
    }

    /*
     * foldRight is right-leaning trees
     *
     *         op: U
     *        /  \
     *    x1: T   op: U
     *           /   \
     *       x2: T    ...
     *                 op: (T,U)=>U
     *                 /  \
     *            xn: T    acc: U
     */
    def foldRight[T,U] (xs: List[T])(acc: U)(op: (T,U) => U): U = xs match {
      case Nil => acc
      case x::xs1 => op(x, foldRight(xs1)(acc)(op))
    }
  }

  object Impl2 {
    /*
     * Implement concat function for two lists.
     * When the result of concat of xs and ys is represented in tree,
     * it's a right leaning tree like as following:
     *              ::
     *             /  \
     *           x1    ::
     *                /  \
     *              x2    ...
     *                     ::
     *                   /   \
     *                 xn +---::----------+
     *                    |  /  \         | this is the acc (a.k.a zero) of the foldRight function
     *                    | y1   ::       |
     *                    |       ...     |
     *                    |        ::     |
     *                    |       /  \    |
     *                    |     yn    Nil |
     *                    +---------------+
     * Therefore, implementation of concat function should be as easy as applying foldRight function as one liner
     */
    def concat[T](xs: List[T], ys: List[T]): List[T] = Impl.foldRight(xs)(ys)(_ :: _)

    /*
     * Quiz: Can `concat` be implemented and/or compiled with foldLeft function, instead of foldRight?
     * Answer: This is a type error.
     * Reason: `op` is of type ((U,T) => U)
     * and now here, U is List[Int] and T is Int
     * `::` operator cannot take Int as the first parameter type and then List[Int] as the second one.
     */
    // def concat[T](xs: List[T], ys: List[T]): List[T] = Impl.foldLeft(xs)(ys)(_ :: _)
  }

  object exercise {
    // Complete the following definitions of the basic functions map and length on lists,
    // such that their implementation uses foldRight

    def mapFun[T, U](xs: List[T], f: T => U): List[U] =
      (xs foldRight List[U]())( f(_) :: _ )

    def lengthFun[T](xs: List[T]): Int =
      (xs foldRight 0)( (_,acc) => acc+1 )
  }
}
