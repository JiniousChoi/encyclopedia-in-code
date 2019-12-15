package week5

object Lecture0504_HigherOrderListFns {
  object Mapping {
    def squareListByPatternMatching(xs: List[Int]): List[Int] = xs match {
      case Nil => Nil
      case x::xs1 => x*x :: squareListByPatternMatching(xs1)
    }

    def squareListByMap(xs: List[Int]): List[Int] = xs map (x => x*x)
  }

  object Filtering {
    def posElemsByPatternMatching(xs: List[Int]): List[Int] = xs match {
      case Nil => Nil
      case x::xs1 => if (x>0) x::posElemsByPatternMatching(xs1) else posElemsByPatternMatching(xs1)
    }

    def posElemsByFilter(xs: List[Int]): List[Int] = xs filter (_>0)
  }

  // more higher-order methods on list
  // group 1: filter, filterNot, partition
  // group 2: takeWhile, dropWhile, span
  object exercise {
    def pack[T](xs: List[T]): List[List[T]] = xs match {
      case Nil => Nil
      case x::xs1 => {
        val (ys, zs) = xs span (_==x)
        ys :: pack(zs)
      }
    }

    def encodeByJin[T](xs: List[T]): List[(T, Int)] = {
      def encode0[T](xss: List[List[T]]): List[(T, Int)] = xss match {
        case List() => Nil
        case xs::xss1 => (xs.head, xs.size) :: encode0(xss1)
      }
      val packed = pack(xs)
      encode0(packed)
    }

    def encodeByMartin[T](xss: List[T]): List[(T, Int)] =
      // all you need is a simple transformation on the result from pack function
      pack(xss) map (xs => (xs.head, xs.length))
  }
}
