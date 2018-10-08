package week5

// How to make msort from the previous lesson0502 polymorphic

object Lecture0503_ImplicitParameters {

  // introduce `less than` function
  object LT {
    def msort[T](xs: List[T])(lt: (T, T) => Boolean): List[T] = xs match {
      case Nil => xs
      case List(_) => xs
      case _ => {
        def merge(xs: List[T], ys: List[T]): List[T] = (xs, ys) match {
          case (Nil, ys) => ys
          case (xs, Nil) => xs
          case (x :: xs1, y :: ys1) => if (lt(x, y)) x :: merge(xs1, ys)
          else y :: merge(xs, ys1)
        }
        val (ys, zs) = xs.splitAt(xs.size / 2)
        merge(msort(ys)(lt), msort(zs)(lt))
      }
    }
  }

  object ORD {
    def msort[T](xs: List[T])(ord: Ordering[T]): List[T] = xs match {
      case Nil => xs
      case List(_) => xs
      case _ => {
        def merge(xs: List[T], ys: List[T]): List[T] = (xs, ys) match {
          case (Nil, ys) => ys
          case (xs, Nil) => xs
          case (x :: xs1, y :: ys1) => if (ord.lt(x, y)) x :: merge(xs1, ys)
          else y :: merge(xs, ys1)
        }
        val (ys, zs) = xs.splitAt(xs.size / 2)
        merge(msort(ys)(ord), msort(zs)(ord))
      }
    }
  }

  object ORD_IMPLICIT {
    def msort[T](xs: List[T])(implicit ord: Ordering[T]): List[T] = xs match {
      case Nil => xs
      case List(_) => xs
      case _ => {
        def merge(xs: List[T], ys: List[T]): List[T] = (xs, ys) match {
          case (Nil, ys) => ys
          case (xs, Nil) => xs
          case (x :: xs1, y :: ys1) => if (ord.lt(x, y)) x :: merge(xs1, ys)
          else y :: merge(xs, ys1)
        }
        val (ys, zs) = xs.splitAt(xs.size / 2)
        merge(msort(ys), msort(zs))
      }
    }
  }
}
